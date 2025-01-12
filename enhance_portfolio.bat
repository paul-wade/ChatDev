@echo off
set BASE_URL=http://localhost:1234/v1
set OPENAI_API_KEY=dummy-key
set CHATDEV_MODEL=codellama-34b-instruct
python run.py --task "Create tests and documentation for Next.js portfolio website. Project is at C:/src/pauls3dminesweeper. Requirements: 1) Jest unit tests for Minesweeper game logic 2) React Testing Library tests for UI components 3) Three.js integration tests for 3D rendering 4) Documentation in markdown format" --name portfolio_docs --model codellama-34b-instruct --modality website
