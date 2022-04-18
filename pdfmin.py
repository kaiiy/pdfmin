import subprocess


def pdfmin(input_filename: str, compression_rate: str = "m"):
    # compression rate (m: medium, h: high; default: m)
    pdf_settings = "/screen" if compression_rate == "h" else "/ebook"

    exec_str = " ".join(
        [
            "gs",
            "-sDEVICE=pdfwrite",
            "-dCompatibilityLevel=1.4",
            f"-dPDFSETTINGS={pdf_settings}",
            "-dNOPAUSE",
            "-dQUIET",
            "-dBATCH",
            f"-sOutputFile={input_filename.rstrip('.pdf')}.min.pdf",
            f"~/Home/pdfmin_py/{input_filename}",
        ]
    )

    # exec
    subprocess.run(exec_str, shell=True)


if __name__ == "__main__":
    pdfmin()
