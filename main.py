import argparse
import chatpdf_api_python.chatpdf_api_python.main as chatpdf

def main():
    # 変数の受け取り
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--api_key', type=str)
    parser.add_argument('-p', '--filepath', type=str)
    args = parser.parse_args()
    
    chatpdf.API_KEY = args.api_key

    file_path_list = [
        args.filepath
    ]

    source_id = chatpdf.upload_files(file_path_list)

    messages = [
        { 'role': 'user', 'content': 'この論文の主張は何？' }
    ]
    reference_sources = True
    response = chatpdf.chat(source_id, messages, reference_sources=reference_sources)
    print(response)


if __name__ == "__main__":
    main()
