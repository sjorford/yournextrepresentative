from pdfminer.pdftypes import PDFException
from sopn_parsing.helpers.pdf_helpers import SOPNDocument
from sopn_parsing.helpers.text_helpers import NoTextInDocumentError


def extract_pages_for_ballot(ballot):
    """
    Try to extract the page numbers for the latest SOPN document related to this
    ballot.

    Because documents can apply to more than one ballot, we also perform
    "drive by" parsing of other ballots contained in a given document.

    :type ballot: candidates.models.Ballot

    """
    try:
        sopn = SOPNDocument(
            file=ballot.sopn.uploaded_file,
            source_url=ballot.sopn.source_url,
            election_date=ballot.election.election_date,
        )
        return sopn.match_all_pages()
    except (NoTextInDocumentError):
        raise NoTextInDocumentError(
            f"Failed to extract pages for {ballot.sopn.uploaded_file.path} as a NoTextInDocumentError was raised"
        )
    except PDFException:
        print(
            f"{ballot.ballot_paper_id} failed to parse as a PDFSyntaxError was raised"
        )
        raise PDFException(
            f"Failed to extract pages for {ballot.sopn.uploaded_file.path} as a PDFSyntaxError was raised"
        )
