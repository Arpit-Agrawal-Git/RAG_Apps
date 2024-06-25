import time

from llmware.library import Library
from llmware.retrieval import Query

input_folder = r"C:\Users\arpit\Desktop\UG\Arpit Agrawal DS\LLMOps\RAG_Apps_Notebooks\Tables_RAG\inputs"
output_folder = r"C:\Users\arpit\Desktop\UG\Arpit Agrawal DS\LLMOps\RAG_Apps_Notebooks\Tables_RAG\outputs"

def parsing_with_pdf():

  t0= time.time()

  lib= Library().create_new_library("first_rag_table_app")

  # parse and extract al content from the pdfs
  parsing_output = lib.add_files(input_folder_path=input_folder)

  print("update: parsing time - ", time.time()-t0)
  print("update: parsing_output - ", parsing_output)

  # to take a look at the content
  # export all content into .jsonl files with metadata
  output1 = lib.export_library_to_jsonl_file(output_folder, "first_parsed_output.jsonl")

  # export all of the tables as csv with 'amazon'
  output2 = Query(lib).export_all_tables(query="vs",output_fp=output_folder)

  return 0


p = parsing_with_pdf()
