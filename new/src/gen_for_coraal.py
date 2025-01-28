import json
from llmtuner import ChatModel
from llmtuner.extras.misc import torch_gc
from tqdm import tqdm
import argparse

def load_chat(chat_path):
    with open(chat_path, 'r') as file:
        data = json.load(file)
    return data

def save_chat(chats, chat_path):
    with open(chat_path, 'w') as file:
        json.dump(chats, file, indent=4)

def main():
    # parser = argparse.ArgumentParser(description="Use for cli file saves")
    # parser.add_argument('--file_path', type=str, required=True, help='The path to the JSON file')
    # parser.add_argument('--out_valid', type=str, required=True, help='The path for the valid JSON output file')
    # # parser.add_argument('--out_invalid', type=str, required=True, help='The path for the invalid JSON output file')
    # parser.add_argument('--key_param', type=str, required=True, help='The JSON key to parse (e.g., LLAMA_response)')

    # args = parser.parse_args()
    exclude_lst =['DCA_textfiles_2018.10.06/DCA_se2_ag2_m_03_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se3_ag2_f_05_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se2_ag2_m_01_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se3_ag2_m_01_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se1_ag1_m_08_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se3_ag2_f_03_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se3_ag2_f_01_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se3_ag2_m_03_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se1_ag2_f_01_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se1_ag2_m_01_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se2_ag2_m_02_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se3_ag2_f_04_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se3_ag2_m_02_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se3_ag2_f_02_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se3_ag1_m_02_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se2_ag1_m_06_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se3_ag3_m_01_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se1_ag1_m_05_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se1_ag4_m_01_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se1_ag1_m_07_2.txt',
                         'DCA_textfiles_2018.10.06/DCA_se2_ag1_f_04_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se3_ag1_m_02_2.txt',
                         'DCA_textfiles_2018.10.06/DCA_se1_ag1_f_05_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se3_ag3_m_01_2.txt',
                         'DCA_textfiles_2018.10.06/DCA_se3_ag3_f_01_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se3_ag1_f_02_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se2_ag1_f_06_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se1_ag1_m_07_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se2_ag1_m_04_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se3_ag3_m_03_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se1_ag1_m_03_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se2_ag3_m_03_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se3_ag1_m_04_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se1_ag3_f_02_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se1_ag1_f_01_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se3_ag1_f_06_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se2_ag1_f_02_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se3_ag1_f_04_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se3_ag4_m_02_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se1_ag1_f_03_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se2_ag3_m_01_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se3_ag1_m_06_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se2_ag1_m_02_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se1_ag1_m_01_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se3_ag1_f_03_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se2_ag1_f_07_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se1_ag4_m_02_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se2_ag4_m_01_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se1_ag1_f_04_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se3_ag3_m_02_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se2_ag1_m_05_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se3_ag1_m_01_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se1_ag1_m_06_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se1_ag1_m_04_1.txt',
                         'DCA_textfiles_2018.10.06/DCA_se2_ag4_f_01_1.txt'
                         ]
    # selected_interviews = ['ROC_textfiles_2020.05/ROC_se0_ag1_m_02_1.txt', 'ATL_textfiles_2020.05/ATL_se0_ag2_m_03_1.txt', 'DCA_textfiles_2018.10.06/DCA_se2_ag2_m_03_1.txt', 'DCA_textfiles_2018.10.06/DCA_se3_ag2_f_05_1.txt','ATL_textfiles_2020.05/ATL_se0_ag2_f_01_1.txt','ROC_textfiles_2020.05/ROC_se0_ag2_f_02_1.txt']
    # selected_interviews = ['ROC_textfiles_2020.05/ROC_se0_ag3_f_02_1.txt', 'VLD_textfiles_2021.07/VLD_se0_ag2_f_01_1.txt', 'ROC_textfiles_2020.05/ROC_se0_ag2_f_04_1.txt', 'ATL_textfiles_2020.05/ATL_se0_ag2_f_01_1.txt', 'DCB_textfiles_2018.10.06/DCB_se1_ag1_f_01_1.txt', 'LES_textfiles_2021.07/LES_se0_ag3_m_01_1.txt', 'PRV_textfiles_2018.10.06/PRV_se0_ag2_m_02_1.txt', 'ROC_textfiles_2020.05/ROC_se0_ag2_m_01_1.txt', 'DTA_textfiles_2023.06/DTA_se1_ag3_m_02_1.txt', 'DCB_textfiles_2018.10.06/DCB_se2_ag1_m_01_1.txt']
    selected_interviews = [
        "ATL_textfiles_2020.05/ATL_se0_ag2_f_01_1.txt",
        "DCB_textfiles_2018.10.06/DCB_se1_ag1_f_01_1.txt",
        "DCB_textfiles_2018.10.06/DCB_se2_ag1_m_01_1.txt",
        "DTA_textfiles_2023.06/DTA_se1_ag3_m_02_1.txt",
        "LES_textfiles_2021.07/LES_se0_ag3_m_01_1.txt",
        "PRV_textfiles_2018.10.06/PRV_se0_ag2_m_02_1.txt",
        "ROC_textfiles_2020.05/ROC_se0_ag2_f_04_1.txt",
        "ROC_textfiles_2020.05/ROC_se0_ag2_m_01_1.txt",
        "ROC_textfiles_2020.05/ROC_se0_ag3_f_02_1.txt",
        "VLD_textfiles_2021.07/VLD_se0_ag2_f_01_1.txt",
        "ATL_textfiles_2020.05/ATL_se0_ag1_f_01_1.txt",
        "DCA_textfiles_2018.10.06/DCA_se1_ag1_f_02_1.txt",
        "DCB_textfiles_2018.10.06/DCB_se1_ag2_f_01_1.txt",
        "DTA_textfiles_2023.06/DTA_se1_ag1_f_01_1.txt",
        "LES_textfiles_2021.07/LES_se0_ag2_f_01_1.txt",
        "PRV_textfiles_2018.10.06/PRV_se0_ag1_f_01_2.txt",
        "ROC_textfiles_2020.05/ROC_se0_ag1_f_02_1.txt",
        "VLD_textfiles_2021.07/VLD_se0_ag3_f_01_2.txt",
        "DTA_textfiles_2023.06/DTA_se1_ag1_f_02_1.txt",
        "ROC_textfiles_2020.05/ROC_se0_ag1_f_03_1.txt",
        "ATL_textfiles_2020.05/ATL_se0_ag1_m_04_2.txt",
        "DCA_textfiles_2018.10.06/DCA_se1_ag3_m_01_1.txt",
        "DCA_textfiles_2018.10.06/DCA_se3_ag4_m_01_1.txt",
        "DCB_textfiles_2018.10.06/DCB_se3_ag3_m_02_1.txt",
        "DTA_textfiles_2023.06/DTA_se1_ag1_m_01_1.txt",
        "DTA_textfiles_2023.06/DTA_se2_ag4_m_02_1.txt",
        "LES_textfiles_2021.07/LES_se0_ag4_m_01_1.txt",
        "VLD_textfiles_2021.07/VLD_se0_ag2_m_01_1.txt",
        "VLD_textfiles_2021.07/VLD_se0_ag3_m_02_1.txt",
        "DCB_textfiles_2018.10.06/DCB_se1_ag2_m_02_1.txt"
    ]

    chat_model = ChatModel()
    messages = []
    print("Welcome to the CLI application, use `clear` to remove the history, use `exit` to exit the application.")
    # file_path = 'new/data/CORAAL_experiments_df_with_prompts.json'
    # file_path = 'new/data/answered_CORAAL_experiments_df_with_prompts.json'
    # file_path = 'new/data/answered_mistral_8x7B_output_CORAAL_experiments_df_with_prompts.json'
    # file_path = 'new/data/answered_Mixtral_8x7B_output_CORAAL_experiments_df_with_prompts.json'
    # -------------------------------------
    # file_path = 'new/data/CORAAL_experiments_df_with_prompts_with_separator_2.json'
    file_path = 'new/data/experiments_df_coraalcomp.json'
    chats = load_chat(file_path)
    modified_episodes = []
    # system_instruction = "Provide a continuation of the guest response last given in an interview using African American English in less than 125 words. Only continue and complete the guest response (do not use of the strings Host: or Guest: in your completion). "
    system_instruction = """
        Instruction for Continuation in African American Vernacular English (AAVE):

            Objective: Extend the last response provided by an interview guest, using African American Vernacular English (AAVE).
            Word Limit: Keep the extension under 125 words.
            Response Guidelines: Ensure that the continuation is a seamless extension of the guest's last response, maintaining the conversational tone and context.
            Exclusion of Labels: Do not include any interview format labels such as "Host:" or "Guest:" in your response.
            Output Requirement: The final output should be a direct continuation of the interview guest's last statement, written as if the guest is still speaking.
    """
    for episode in tqdm(chats, desc="Processing episodes"):
        if episode['episode_id'] not in exclude_lst:
            if episode['episode_id'] in selected_interviews:
                messages = []
                print(f"episode ID: {episode['episode_id']}" )
                for conversation in tqdm(episode['conversations'], desc=f"Processing conversations for {episode['episode_id']}"):
                    # system = conversation['system_instruction']
                    system = system_instruction
                    sender = conversation['host_role']
                    message = conversation['prompt_info']
                    gt_res = conversation['guest_gt']
                    cor_res = conversation['CORAAL_continuation']
                    print(f"{sender}: {message}")

                    # if sender == 'user':
                    response = ""
                    messages.append({"role": "user", "content": message})
                    for new_text in chat_model.stream_chat(messages,system=system,top_p=0.8,top_k=50,temperature=0.90,repetition_penalty=1.2,max_new_tokens=45):
                        response += new_text
                    conversation["Mixtral-8x7B-responses"] = response
                    print(f"Assistant: {response}")
                    print(f"GT Res: {cor_res}")

                    messages.append({"role": "assistant", "content": cor_res})
                    # messages.append({"role": "assistant", "content": gt_res})
                modified_episodes.append(episode)
                
        print("------")
    new_file_path = 'new/data/answered_mistral8x7B_selected30_new_prompt_coraal_history.json'
    save_chat(modified_episodes, new_file_path)

    
if __name__ == "__main__":
    main()