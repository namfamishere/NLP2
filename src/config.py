from transformers import BertTokenizer

DEVICE = "cuda"
MAX_LEN = 512
TRAIN_BATCH_SIZE = 8
VALID_BATCH_SIE = 4
EPOCHS = 10
ACCUMULATION = 2
BERT_PATH = "./input/bert-base-uncased"
MODEL_PATH = "model.bin"
TRAINING_FILE = "./input/IMDB Dataset.csv"
TOKENIZER = BertTokenizer.from_pretrained(
    BERT_PATH, 
    do_lower_case=True)
