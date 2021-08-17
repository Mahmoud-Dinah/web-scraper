from web_scraper.scraper import *


def test_get_citations_needed_count():
    expected=5
    actual=get_citations_needed_count(requests_url)
    assert expected==actual


def test_get_citations_needed_report():
    assert get_citations_needed_report(requests_url)           
    
