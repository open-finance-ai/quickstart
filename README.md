# Open Finance quickstart

This repository accompanies Open Finance's [**quickstart guide**][quickstart].

Here you'll find full example integration with various coding languages.

This Quickstart is designed to show you how to integrate to our api's using basic code

## 1. Clone the repository

Using https:

```bash
git clone https://github.com/open-finance/quickstart
cd quickstart
```

Alternatively, if you use ssh:

```bash
git clone git@github.com:open-finance/quickstart.git
cd quickstart
```

## 2. Set up your environment variables

```bash
cp .env.example .env
```

Copy `.env.example` to a new file called `.env` and fill out the environment variables inside. At
minimum `OF_CLIENT_ID` and `OF_CLIENT_SECRET` must be filled out. Get your Client ID and secrets from
the dashboard: https://dashboard.open-finance.ai

> NOTE: `.env` files are a convenient local development tool. Never run a production application
> using an environment file with secrets in it.

## 3. Run the Quickstart

#### Pre-requisites

- The language you intend to use is installed on your machine and available at your command line.
  This repo should generally work with active LTS versions of each language such as python >= 3.9
- Your environment variables populated in `.env`

#### 1. Running the backend


##### Python

**:warning: As `python2` has reached its end of life, only `python3` is supported.**

```bash

# If you use virtualenv
# virtualenv venv
# source venv/bin/activate

pip install -r requirements.txt
python open-finance.py
```

## Test credentials

For testing purposes, you can log in to to a fake provider (Open Finance Bank) using the id one of the id's from the docs - https://docs.open-finance.ai. If you are prompt for login use `user` as Username and `pass` as Password

In Production, use real-life credentials and do not forget to remove the `includeFakeProvider: true` parameter from connection creation.
