export CUDA_VISIBLE_DEVICES=2
fold=1
rm -rf model_roberta_wwm_ext
for((i=0;i<$fold;i++));  
do   

python run_bert.py \
--seed 4321 \
--model_type bert \
--model_name_or_path ./pretrained_model/chinese_roberta_wwm_ext \
--do_test \
--do_train \
--do_eval \
--data_dir ./data/data_$i \
--output_dir ./model_roberta_wwm_ext/model_roberta_wwm_ext$i \
--max_seq_length 510 \
--split_num 1 \
--lstm_hidden_size 1024 \
--lstm_layers 1 \
--lstm_dropout 0.5 \
--eval_steps 200 \
--per_gpu_train_batch_size 4 \
--gradient_accumulation_steps 4 \
--warmup_steps 0 \
--per_gpu_eval_batch_size 32 \
--learning_rate 3e-6 \
--adam_epsilon 1e-6 \
--weight_decay 0.007 \
--train_steps 30000 

done  
  

echo "save models into backup fold"
t=`date +%Y%m%d%H%M%S`
cp -rf ./model_roberta_wwm_ext backup-models/roberta_wwm_ext_models/models-$t
echo "done"

rm result.csv
echo "combine result"
python combine.py --model_prefix model_roberta_wwm_ext/model_roberta_wwm_ext --out_path result.csv --fold $fold
echo "done"

echo "save result into backup fold"
cp result.csv backup-models/roberta_wwm_ext_models/models-$t
echo "done"

echo "save run script into backup fold"
cp run_roberta_wwm_ext.sh backup-models/roberta_wwm_ext_models/models-$t

