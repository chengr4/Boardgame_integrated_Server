from abc import ABC, abstractmethod

# This is an abstract class
class Crawler(ABC):

  @abstractmethod
  def fetchHTML(self): pass