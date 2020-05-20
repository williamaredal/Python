from sec_edgar_downloader import Downloader

dl = Downloader('C:\\Users\\willi\\Documents\\Company_filings\\BRK-A\\13F-HR')

# Downloads using CIK of Berkshire hathaway BERK-A
dl.get("13F-HR", "0001067983")
