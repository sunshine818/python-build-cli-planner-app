#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 18:58:06 2020

@author: luca
"""

from abc import ABC, ABCMeta, abstractmethod
from collections.abc import Iterable
from dateutil.parser import parse
from datetime import datetime

class DeadlinedMetaReminder(Iterable, metaclass=ABCMeta):
    @abstractmethod
    def is_due(self):
        pass
    
class DeadlinedReminder(ABC, Iterable):
    @abstractmethod
    def is_due(self):
        pass
    
class DateReminder(DeadlinedReminder):
    def __init__(self, text, date):
        self.date = parse(date, dayfirst=True)
        self.text = text
        
    def is_due(self):
        return self.date <= datetime.now
    
    def __iter__(self):
        return iter([self.text, self.date.isoformat()])