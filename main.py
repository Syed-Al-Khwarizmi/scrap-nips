# -*- coding: utf-8 -*-

from papers import Papers

def main():
    paper = Papers()
    paper_filter = paper.filter()
    list_papers = [paper for sublist in paper_filter for paper in sublist if '/paper/' in paper]
    papers = ['{}.pdf'.format(x) for x in list_papers]
    for p in papers:
        paper.download(p)

if __name__ == "__main__":
    main()