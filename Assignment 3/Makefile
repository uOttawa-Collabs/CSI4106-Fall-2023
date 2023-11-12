TEX_FILENAME = main
TEX_FILE = $(TEX_FILENAME).tex
PDF_FILE = $(TEX_FILENAME).pdf

PYTHON_PLOT_SCRIPTS = Q3.plot.py
SVG_FIGURES = Figure.3.1.svg Figure.3.2.svg Figure.3.3.svg
FODG_FIGURES = Figure.6.fodg
SVG_FIGURES_PDF = $(SVG_FIGURES:.svg=.pdf)
FODG_FIGURES_PDF = $(FODG_FIGURES:.fodg=.pdf)

all: $(PDF_FILE)

$(PDF_FILE): $(TEX_FILE) $(SVG_FIGURES_PDF) $(FODG_FIGURES_PDF)
	pdflatex $(TEX_FILE)
	bibtex $(TEX_FILENAME)
	pdflatex $(TEX_FILE)
	pdflatex $(TEX_FILE)

%.pdf: %.svg
	inkscape --export-filename=$@ $<

%.pdf: %.fodg
	soffice --headless --convert-to pdf $<

$(SVG_FIGURES): $(PYTHON_PLOT_SCRIPTS)
	python3 $<

$(SVG_FIGURES_PDF): $(SVG_FIGURES)

$(FODG_FIGURES_PDF): $(FODG_FIGURES)

clean:
	rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb *.lof *.bbl *.blg *.gz $(SVG_FIGURES) $(SVG_FIGURES_PDF) $(FODG_FIGURES_PDF)

cleanall: clean
	rm -f $(PDF_FILE)

.PHONY: all clean cleanall
