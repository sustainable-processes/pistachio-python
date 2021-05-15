import requests
from urllib.error import HTTPError


class Pistachio:
    def __init__(self, base_url: str = "http://localhost:8898/"):
        self.base_url = base_url
        self.session_id = None

    def __enter__(self):
        self.renew_session()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_session()

    def parse(self, query: str) -> dict:
        """
        Parse a textual query without running a search.
        The normalized terms and their character offsets in the original text are reported.

        Parameters
        ----------
        query : str
            A query to parse

        Returns
        -------
        response_dict : dict
            A dictionary with the response

        """
        return self._get("parse", {"q": query})

    def suggest(self, query: str) -> dict:
        """
        Generate suggestions for the input text.

        Parameters
        ----------
        query : str
            A query to parse

        Returns
        -------
        response_dict : dict
            A dictionary with the response

        """
        return self._get("suggest", {"q": query})

    def search(
        self,
        query: str,
        reaction_grouping: bool = True,
        begin_offset: int = 0,
        end_offset: int = 0,
        draw: int = 0,
    ) -> dict:
        if self.session_id is None:
            raise ValueError("Session id is null. Call renew_session")
        payload = dict(
            q=query,
            s=self.session_id,
            g=reaction_grouping,
            b=begin_offset,
            e=end_offset,
            d=draw,
        )
        return self._get("search", params=payload)

    def get_details(self, reaction_id: str) -> dict:
        """Get the details of a reaction"""
        r = requests.get(self.base_url + "get/" + reaction_id)
        if r.status_code == 200:
            return r.json()

        else:
            raise HTTPError(f"Got response code: {r.status_code}")

    def summary(
        self, query: str, reaction_grouping: bool = True, draw: int = 0
    ) -> dict:
        if self.session_id is None:
            raise ValueError("Session id is null. Call renew_session")
        payload = dict(q=query, s=self.session_id, g=reaction_grouping, d=draw)
        return self._get("summary", params=payload)

    def renew_session(self):
        r = requests.get(self.base_url + "newsessionid")
        if r.status_code == 200:
            self.session_id = int(r.text)
        else:
            raise HTTPError(f"Got responsse code: {r.status_code}")

    def end_session(self):
        if self.session_id is None:
            raise ValueError("Session id is null. Call renew_session")
        self._get("endsession", params={"s": self.session_id})

    def _get(self, endpoint: str, params: dict = None) -> dict:
        r = requests.get(self.base_url + endpoint, params=params)
        if r.status_code == 200:
            return r.json()
        else:
            raise HTTPError(f"Got response code: {r.status_code}")
