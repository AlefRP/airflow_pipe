from airflow.plugins_manager import AirflowPlugin
from airflow.hooks.base import BaseHook

from elasticsearch import Elasticsearch

class ElasticHook(BaseHook):
    """
    A hook for connecting to an Elasticsearch instance.

    This hook provides a connection to an Elasticsearch instance using the provided connection ID.
    It inherits from the `BaseHook` class and extends its functionality.

    Attributes:
        conn_id (str): The ID of the Elasticsearch connection to use.

    Methods:
        __init__(self, conn_id="elastic_default", *args, **kwargs): Initializes an instance of the `ElasticHook` class.
            Args:
                conn_id (str): The ID of the Elasticsearch connection to use.
                *args: Additional positional arguments.
                **kwargs: Additional keyword arguments.
    """

    def __init__(self, conn_id="elastic_default", *args, **kwargs):
        """
        Initializes an instance of the ElasticHook class.

        :param conn_id: The connection ID to use for the Elasticsearch connection. Defaults to "elastic_default".
        :type conn_id: str
        :param args: Additional positional arguments.
        :type args: Any
        :param kwargs: Additional keyword arguments.
        :type kwargs: Any
        """
        super().__init__(*args, **kwargs)
        coon = self.get_connection()
        
        conn_config = {}
        hosts = []
        
        if coon.host:
            hosts = coon.host.split(",")
        if coon.port:
            conn_config["port"] = int(coon.port)
        if coon.username:
            conn_config["http_auth"] = (coon.username, coon.password)
        
        self.es = Elasticsearch(hosts, **conn_config)
        self.index = coon.schema
        
    def info(self):
        """
        Returns information about the Elasticsearch instance.

        :return: A dictionary containing information about the Elasticsearch instance.
        """
        return self.es.info()
    
    def set_index(self, index):
        """
        Sets the index of the object.

        Args:
            index (str): The index to be set.

        Returns:
            None
        """
        self.index = index
        
    def add_doc(self, index, doc_type, doc):
        """
        Adds a document to the specified index in Elasticsearch.

        Args:
            index (str): The name of the index where the document will be added.
            doc_type (str): The type of the document.
            doc (dict): The document to be added.

        Returns:
            dict: The response from the Elasticsearch index API.
        """
        self.set_index(index)
        res = self.es.index(index=index, doc_type=doc_type, body=doc)
        return res
    
class AirflowElasticPlugin(AirflowPlugin):
    """
    A plugin for integrating Elasticsearch with Apache Airflow.

    Attributes:
        name (str): The name of the plugin, set to "elastic".
        hooks (list): A list containing the ElasticHook class for interacting with Elasticsearch.
    """
    name = "elastic"
    hooks = [ElasticHook]