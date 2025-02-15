# **AAE Project**

A project for analyzing, and generating text responses using LLMs with a focus on **African American English (AAE)**.

---
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97-Hugging%20Face%20Collection-blue)](https://huggingface.co/collections/kweCobi/aaemine-67aa4f38ad0860d669105f41)
[![arXiv](https://img.shields.io/badge/arXiv-2502.04564-b31b1b.svg)](https://arxiv.org/abs/2502.04564)
## **Abstract**

## **Setup**
To set up the project environment, follow these steps:

### **1. Create and activate the conda environment**
Run the `setup.sh` script:
```bash
source setup.sh
```

This will:
	-	Create a conda environment called aae
	-	Activate it
	-	Install all necessary dependencies

### **1. Install additional dependencies (if needed)***
If you need to manually install dependencies, run:
```conda env create -f environment.yml
conda activate aae
```

## **Running Text Generation and Fine-Tuning**

### **1. Prepare LLMTuner (LlamaFactory)**

Download ([LLamaFactory](https://github.com/hiyouga/LLaMA-Factory)) (formerly known as LLMTuner) and place the src folder inside your project as llmtuner:
```cp -r /path/to/llmtuner/src AAE/new/src/llmtuner```


### **2. Generate Text Responses**

Run the script to generate responses from the base model:
```bash AAE/new/scripts/run_generations.sh```
This script:
	-	Runs the base model to generate responses to interviewer questions.
	-	Allows modifying the system prompt in the script if needed.


## **Data Processing & Analysis**
	•	T-Statistics Analysis (T-Stats_Analysis_Files/)
	•	Contains survey-based R analysis scripts.
	•	Data files from different survey responses, labeled for statistical analysis.


Citation

If you use this project code in your research, 

please kindly cite as:
```
@misc{sandoval2025llmmimicaae,
      title={My LLM might Mimic AAE -- But When Should it?}, 
      author={Sandra C. Sandoval and Christabel Acquaye and Kwesi Cobbina and Mohammad Nayeem Teli and Hal Daumé III},
      year={2025},
      eprint={2502.04564},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2502.04564}, 
}
```

and also please cite the following sources:
LLamafactory
```
@inproceedings{zheng2024llamafactory,
  title={LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models},
  author={Yaowei Zheng and Richong Zhang and Junhao Zhang and Yanhan Ye and Zheyan Luo and Zhangchi Feng and Yongqiang Ma},
  booktitle={Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations)},
  address={Bangkok, Thailand},
  publisher={Association for Computational Linguistics},
  year={2024},
  url={http://arxiv.org/abs/2403.13372}
}
```

AAE Datasets
```
	@article{Kendall2020CORAAL,
    author = {Kendall, Tyler and Farrington, Charlie},
    title = {CORAAL: The Corpus of Regional African American Language},
    year = {2020},
    url = {https://oraal.uoregon.edu/coraal}
    }

    @inproceedings{Blodgett2017AAE,
    author = {Blodgett, Su Lin and O’Connor, Brendan},
    title = {Racial Disparity in Natural Language Processing: A Case Study of Social Media African-American English},
    booktitle = {Proceedings of the Fairness, Accountability, and Transparency in Machine Learning},
    year = {2017}
    }
```
### ***Acknowledgments***

This project builds upon CORAAL, MUSE, and Tweet datasets for language analysis and aims to improve cultural representation in NLP.

We gratefully acknowledge the support of TRAILS (The Institute for Trustworthy AI in Law & Society) for funding this project.
