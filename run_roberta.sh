export CUDA_VISIBLE_DEVICES=2
fold=1
rm -rf model_roberta
for((i=0;i<$fold;i++));  
do   

python run_bert.py \
--seed 4321 \
--model_type bert \
--model_name_or_path pretrained_model/chinese_roberta \
--do_train \
--do_eval \
--do_test \
--data_dir ./data/data_$i \
--output_dir ./model_roberta/model_roberta$i \
--max_seq_length 168 \
--split_num 5 \
--lstm_hidden_size 1024 \
--lstm_layers 3 \
--lstm_dropout 0.5 \
--eval_steps 200 \
--per_gpu_train_batch_size 4 \
--gradient_accumulation_steps 4 \
--warmup_steps 0 \
--per_gpu_eval_batch_size 32 \
--learning_rate 2e-6 \
--adam_epsilon 1e-6 \
--weight_decay 0.005 \
--train_steps 25000

done  

echo "save models into backup fold"
t=`date +%Y%m%d%H%M%S`
cp -rf ./model_roberta backup-models/roberta_models/models-$t
echo "done"

rm result.csv
echo "combine result"
python combine.py --model_prefix model_roberta/model_roberta --out_path result.csv --fold $fold
echo "done"

echo "save result into backup fold"
cp result.csv backup-models/roberta_models/models-$t
echo "done"

echo "save run script into backup fold"
cp run_roberta.sh backup-models/roberta_models/models-$t

