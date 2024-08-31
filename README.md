# Splash

A sweet way to convert your markdown files into HTML. 👌🏽

## Description

A python command line application that takes markdown files in a folder and convert them to HTML using a template file `./template.html` and saves the html files in the public folder.

### Please Note

For each time the application is run, the public folder is emptied and then filled.

## Getting Started

### Git clone

`git clone https://github.com/see-why/splash.git`

### Dependancies

Ensure you have [Python3](https://www.python.org/downloads/) installed.

Confirm this by running:
- On macOS/Linux: `which python3`
- On Windows: `python --version` or `py --version`

### Running program

- To start run `(zsh or bash) main.sh` (if you have trouble executing, you might what to change the file permission so it's treated as an executable file using `chmod`)
- Voila!!!, you should see a public folder with the corresponding HTML.
- You can `cd public` and start the http server `python3 -m http.server 8889` then open http://localhost:8889/ to see the default files genereted using the files shipped with the application.
- run `(zsh or bash) test.sh` for tests.
- Add your markdown files (could be directories or just files) to the Content folder.
- For images and css, please add them to the static folder.
- run the start command and enjoy!!!.

## Author
👤 **Cyril Iyadi**

- GitHub: [@see-why](https://github.com/see-why)
- LinkedIn: [C.Iyadi](https://www.linkedin.com/in/cyril-iyadi/)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](../../issues/).

## Show your support

Give a ⭐️ if you like this project!

## 📝 License
- This project is [MIT](./LICENSE) licensed.