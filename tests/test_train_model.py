# tests/test_train_model.py
import os
import subprocess

def test_model_file_created():
    # Run the training script
    subprocess.run(["python", "train/train_model.py"], check=True)
    
    # Check if the model file exists
    assert os.path.exists("model/model.pkl"), "model.pkl was not created"