import os
import pandas as pd
import argparse
import chatpdf_api_python.chatpdf_api_python.main as chatpdf

def main():
    # 変数の受け取り
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--api_key', type=str)
    parser.add_argument('-p', '--filepath', type=str)
    args = parser.parse_args()

    questions_path = os.path.join('.', 'questions.csv')
    df_questions = pd.read_csv(questions_path, header=None)
    question_list = df_questions[0].values.tolist()
    # print(question_list)

    chatpdf.API_KEY = args.api_key

    file_path_list = [
        args.filepath
    ]

    source_id = chatpdf.upload_files(file_path_list)
    for question in question_list:
        question = '日本語で答えてください．'+question
        messages = [
            { 'role': 'user', 'content': question}
        ]
        reference_sources = True
        response = chatpdf.chat(source_id, messages, reference_sources=reference_sources)
        print(response)
        print()


if __name__ == "__main__":
    main()
