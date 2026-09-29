from ingestion.loader import load_documents
from ingestion.parser import parse_json
from ingestion.transformer import transform_documents
def main():
    text = load_documents("data/candidate.json")
    parser = parse_json(text)
    documents = transform_documents(parser)

    for document in documents:
        print(document)

if __name__ == "__main__":
    main()