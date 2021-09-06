# NodeJS Adhan Alert

This application is made for NodeJS. It is a system that runs the adhan on a specific time.
## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

What things you need and what to install and how to install them on your own RPi

#### Hardware
* A Raspberry Pi (any). This is the one I [have](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/)

#### Software

* [Git](https://git-scm.com/)
* [Ubuntu](https://releases.ubuntu.com/20.04/)
* NodeJS
* Typescript
* [VLC](https://linuxize.com/post/how-to-install-vlc-on-ubuntu-20-04/) 


### Installing

A step by step series of examples that tell you how to start using the application.

In your folder, firstly clone the repository, using HTTPS or SSH
```bash
# The following command is to clone the repository using HTTPS
git clone https://github.com/yassine955/adhan-js.git

# The following comment is to clone the repository using SSH (recommended)
git clone git@github.com:yassine955/adhan-js.git
```

When you succesfully cloned the repository, change the directory to the repository using: `cd adhan-js/`, then you're in the right folder, install the necessary packages that's inside the requirements.txt file

```bash
npm install
```

Go inside the `src/functions/fetchAPI.ts` and change `/Niederlande/Leiden%20(S%C3%BCdholland).txt` to `/<your country>/<city>`

The API I used for this is the same API my local mosque uses, click [here](https://izaachen.de/api/times/2021/) to view the API.

After all of this

```bash
tsc
```

```bash
node dist/index.js
```


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
