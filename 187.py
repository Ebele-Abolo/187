text_file = filldialog.askopenfilename(title=" Open Text File",
	filetypes=(("Text Files", "*.txt")))
name = os.path.basename(text_file)
byte_str = bytes.fromhex(paragraph)
orignal = decrypt('XYZ', byte_str)
final_data = orginal.decode("utf-8")
text_file.close()