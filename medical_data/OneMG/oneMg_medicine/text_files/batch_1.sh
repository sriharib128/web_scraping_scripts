#!/bin/bash
#SBATCH --job-name=train_new_1
#SBATCH --output=Mal.out
#SBATCH --mail-user=venkata.kesav@students.iiit.ac.in
#SBATCH --mail-type=ALL
# SBATCH -A venkata_kesav
#SBATCH --partition=long
#SBATCH -c 10
#SBATCH --mem-per-cpu=2048
#SBATCH --time=4-00:00:00
#SBATCH --gres=gpu:1
#SBATCH -w gnode007
echo "loading cuda, cudnn modules"

echo "running python script"
python3 /home2/venkata_kesav/home2/Code/cropper.py
echo "Execution completed"
deactivate
echo "------END------"

