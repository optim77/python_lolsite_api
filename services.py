import os
import requests
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps


def stats():

    try:
        api_key = os.environ.get("API_KEY")
        url = f"https://api.pandascore.co/lol/champions?token={api_key}"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None
    try:
        quote = response.json()
        return quote
    except (KeyError, TypeError, ValueError):
        return None


def get_character(ch):
    try:
        api_key = os.environ.get("API_KEY")
        url = f"https://api.pandascore.co/lol/champions?token={api_key}&filter[name]=" + ch
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None
    try:
        quote = response.json()
        return quote
    except (KeyError, TypeError, ValueError):
        return None


def get_items():
    try:
        api_key = os.environ.get("API_KEY")
        url = f"https://api.pandascore.co/lol/items?token={api_key}"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None
    try:
        quote = response.json()
        return quote
    except (KeyError, TypeError, ValueError):
        return None


def get_item(name):
    try:
        api_key = os.environ.get("API_KEY")
        url = f"https://api.pandascore.co/lol/items/{name}?token={api_key}"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None
    try:
        quote = response.json()
        return quote
    except(KeyError, TypeError, ValueError):
        return None


def get_all_life():
    try:
        api_key = os.environ.get("API_KEY")
        url = f"https://api.pandascore.co/lol/matches/running?token={api_key}"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None
    try:
        quote = response.json()
        return quote
    except(KeyError, TypeError, ValueError):
        return None


def upcoming():
    try:
        api_key = os.environ.get("API_KEY")
        url = f"https://api.pandascore.co/lol/matches/upcoming?token={api_key}"
        resposne = requests.get(url)
        resposne.raise_for_status()
    except requests.RequestException:
        return None
    try:
        quote = resposne.json()
        return quote
    except(KeyError, TypeError, ValueError):
        return None

def get_teams():
    try:
        api_key = os.environ.get("API_KEY")
        url = f"https://api.pandascore.co/lol/teams?token={api_key}"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None
    try:
        quote = response.json()
        return quote
    except(KeyError, TypeError, ValueError):
        return None


def get_team(name):
    try:
        api_key = os.environ.get("API_KEY")
        url = f"https://api.pandascore.co/lol/teams?token={api_key}&search[slug]={name}"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None
    try:
        quote = response.json()
        return quote
    except(KeyError, TypeError, ValueError):
        return None


def get_tournaments():
    try:
        api_key = os.environ.get("API_KEY")
        url = f"https://api.pandascore.co/lol/tournaments/running?token={api_key}"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None
    try:
        quote = response.json()
        return quote
    except(KeyError, TypeError, ValueError):
        return None


def get_player(name):
    try:
        api_key = os.environ.get("API_KEY")
        url = f"https://api.pandascore.co/lol/players?token={api_key}&search[slug]={name}"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None
    try:
        quote = response.json()
        return quote
    except(KeyError, TypeError, ValueError):
        return None