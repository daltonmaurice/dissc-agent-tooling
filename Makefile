# Makefile for building AI-Powered Economic Research workflows presentation
# This Makefile provides targets to build the Quarto presentation into different formats

# Variables
PRESENTATION = agents-tooling-mcp.qmd
OUTPUT_DIR = output
REVEALJS_OUTPUT = $(OUTPUT_DIR)/agents-tooling-mcp.html
BEAMER_OUTPUT = $(OUTPUT_DIR)/agents-tooling-mcp.pdf

# Default target
.PHONY: all
all: revealjs

# Create output directory
$(OUTPUT_DIR):
	mkdir -p $(OUTPUT_DIR)

# Build RevealJS HTML presentation
.PHONY: revealjs
revealjs: $(OUTPUT_DIR)
	@echo "Building RevealJS HTML presentation..."
	quarto render $(PRESENTATION) --to revealjs --output-dir $(OUTPUT_DIR)
	@echo "✅ RevealJS presentation built: $(REVEALJS_OUTPUT)"

# Build Beamer PDF presentation
.PHONY: beamer
beamer: $(OUTPUT_DIR)
	@echo "Building Beamer PDF presentation..."
	quarto render $(PRESENTATION) --to beamer --output-dir $(OUTPUT_DIR)
	@echo "✅ Beamer PDF presentation built: $(BEAMER_OUTPUT)"

# Build both formats
.PHONY: both
both: revealjs beamer
	@echo "✅ Both presentations built successfully!"

# Preview the RevealJS presentation in browser
.PHONY: preview
preview: revealjs
	@echo "Opening RevealJS presentation in browser..."
	open $(REVEALJS_OUTPUT)

# Clean output files
.PHONY: clean
clean:
	@echo "Cleaning output files..."
	rm -rf $(OUTPUT_DIR)
	@echo "✅ Cleaned output directory"

# Check if Quarto is installed
.PHONY: check-quarto
check-quarto:
	@echo "Checking if Quarto is installed..."
	@which quarto > /dev/null || (echo "❌ Quarto is not installed. Please install it from https://quarto.org/docs/get-started/" && exit 1)
	@echo "✅ Quarto is installed: $$(quarto --version)"

# Install Quarto (macOS with Homebrew)
.PHONY: install-quarto
install-quarto:
	@echo "Installing Quarto via Homebrew..."
	brew install --cask quarto
	@echo "✅ Quarto installed successfully"

# Serve the presentation locally (for development)
.PHONY: serve
serve: revealjs
	@echo "Serving presentation locally at http://localhost:4200"
	@echo "Press Ctrl+C to stop the server"
	cd $(OUTPUT_DIR) && python3 -m http.server 4200

# Help target
.PHONY: help
help:
	@echo "Available targets:"
	@echo "  all          - Build RevealJS presentation (default)"
	@echo "  revealjs     - Build HTML presentation with RevealJS"
	@echo "  beamer       - Build PDF presentation with Beamer"
	@echo "  both         - Build both HTML and PDF presentations"
	@echo "  preview      - Build and open RevealJS presentation in browser"
	@echo "  serve        - Build and serve presentation locally"
	@echo "  clean        - Remove all output files"
	@echo "  check-quarto - Check if Quarto is installed"
	@echo "  install-quarto - Install Quarto via Homebrew (macOS)"
	@echo "  help         - Show this help message"

# Dependencies
$(REVEALJS_OUTPUT): $(PRESENTATION) | $(OUTPUT_DIR)
$(BEAMER_OUTPUT): $(PRESENTATION) | $(OUTPUT_DIR)
