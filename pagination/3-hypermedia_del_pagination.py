#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination

This script implements a deletion resilient hypermedia
pagination system for a database of popular baby names.
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.

    Attributes:
        DATA_FILE (str): The file path of the popular
        baby names dataset.
        __dataset (List[List]): A cached list of lists
        representation of the dataset.
        __indexed_dataset (Dict[int, List]): A cached
        dictionary of thedataset indexed by sorting position.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initialize the Server object and set the cached
        dataset and indexed_dataset to None.
        """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Return the cached dataset or load it from the
        DATA_FILE if it is not yet cached.

        Returns:
            List[List]: The dataset as a list of lists.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Return the cached indexed_dataset or create
        it from the dataset if it is not yet cached.

        Returns:
            Dict[int, List]: The dataset indexed by sorting position.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
                }

        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a hypermedia index of the dataset
        """
        if index is None:
            index = 0
        assert 0 <= index < len(self.__indexed_dataset)

        next_index = index + page_size
        data = []

        for i in range(index, min(next_index, len(self.__indexed_dataset))):
            if i in self.__indexed_dataset:
                data.append(self.__indexed_dataset[i])

        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data,
        }
