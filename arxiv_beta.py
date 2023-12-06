import os
import arxiv
import json

def fetch_ml_papers():
# Define the categories
    categories = [
        "cs.AI"
        "cs.CL",
        "cs.CV",
    ]  # Computer Science, Machine Learning, Artificial Intelligence

    # Define a directory to save the downloaded PDFs
    download_dir = "arxiv_pdfs"
    os.makedirs(download_dir, exist_ok=True)

    # Search and download papers
    for category in categories:
        search_results = arxiv.Search(
            query=f"cat:{category}",
            sort_by=arxiv.SortCriterion.SubmittedDate,
            sort_order=arxiv.SortOrder.Descending,
        )  # You can adjust max_results
        c = 0
        for result in arxiv.Client().results(search_results):
            c += 1
            print(result.title)
            result.download_pdf(dirpath="./mydir", filename=f"paper_{c}.pdf")
            
            # save the metadata for the first paper in a json format
            metadata_dict = {
                "entry_id": f"{result.entry_id}",
                "updated": f"{result.updated}",
                "published": f"{result.published}",
                "title": f"{result.title}",
                "authors": f"{','.join([x.name for x in result.authors])}",  # Join author names with a comma and space
                "summary": f"{result.summary}",
                "comment": f"{result.comment}",
                "journal_ref": f"{result.journal_ref}",
                "doi": f"{result.doi}",
                "primary_category": f"{result.primary_category}",
                "categories": f"{result.categories}",  # Join categories with a comma and space
                "links": f"{','.join([x.href for x in result.links])}",  # Join links with a comma and space
                "pdf_url": f"{result.pdf_url}",
            }


            metadata_dir = 'metadata'

            # Ensure the directory exists or create it if it doesn't
            os.makedirs(metadata_dir, exist_ok=True)

            # Create a JSON file path within the directory
            metadata_file_path = os.path.join(metadata_dir, f'metadata_{c}.json')

            # Dump the metadata dictionary to a JSON file
            with open(metadata_file_path, 'w') as metadata_file:
                json.dump(metadata_dict, metadata_file, indent=4)


if __name__ == "__main__":
    fetch_ml_papers()