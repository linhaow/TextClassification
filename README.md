作者ustc-linhw

本文件为文本分类任务

比赛解题报告会在知乎和公众号上更新

知乎：https://www.zhihu.com/people/lhw-55

公众号：纸鱼AI

![avatar](https://pic2.zhimg.com/80/v2-aa1e864f55284a12336b7132b91b0b9d_hd.jpg)

代码是基于郭大的开源代码修改的

目前支持的功能如下：

—— 训练数据集kfold处理

—— 训练数据集数据信息查看

—— 使用预训练模型进行文本分类

    —— roberta_wwm_ext_large

    —— roberta_large

    —— xlnet_large (to do)

—— 不同模型结果进行投票ensemble

—— 对于训练完成的模型自动保存模型，配置以及输出结果

主要文件目录如下：

—— backup-models:自动存档目录，输出的模型和结果会自动存档到该目录

—— data：数据文件，用于存放训练用的数据，在该文件下数据分析，数据kfold处理

—— pretrained_model: 用于存放预训练的模型

—— run_xxxxx.sh: 训练某个模型所使用的bash文件

—— run_xxxx.py: 具体的训练代码

—— ensemble_submits：对输出的result文件进行vote融合结果


具体使用流程


1. 对于不同的分类任务，可能需要修改下述文件，目前是2分类，如要修改，修改下述文件。

—— preprocess.py

—— run_bert.py

    —— 标签label

    —— 类别数

    —— 类别loss

—— combine.py


2. cd data && python analysis.py 查看数据集的相关情况

3. python preprocess.py 完成数据预处理，并且将数据分成kfold

4. 修改run_xxxx.sh文件设置参数

    注：该模型将文本截成k段，分别输入语言模型，然后顶层用GRU拼接起来。好处在于设置小的max_length和更大的k来降低显存占用，因为显存占用是关于长度平方级增长的，而关于k是线性增长

    1)实际长度 = max_seq_length * split_num

    2)实际batch size 大小= per_gpu_train_batch_size * numbers of gpu

    3)上面的结果所使用的是4卡GPU，因此batch size为4。如果只有1卡的话，那么per_gpu_train_batch_size应设为4, max_length设置小一些。

    4)如果显存太小，可以设置gradient_accumulation_steps参数，比如gradient_accumulation_steps=2，batch size=4，那么就会运行2次，每次batch size为2，累计梯度后更新，等价于batch size=4，但速度会慢两倍。而且迭代次数也要相应提高两倍，即train_steps设为10000

    具体batch size可看运行时的log，如：

    09/06/2019 21:03:41 - INFO - __main__ -   ***** Running training *****

    09/06/2019 21:03:41 - INFO - __main__ -     Num examples = 5872

    09/06/2019 21:03:41 - INFO - __main__ -     Batch size = 4

    09/06/2019 21:03:41 - INFO - __main__ -     Num steps = 5000

5. 最后输出文件会生成result.csv，模型会在对应的模型文件夹中生成，backup文件夹问自动保存对应的模型。


