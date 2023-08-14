<!-- badges: start -->

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/license/apache-2-0/)[![Lifecycle:Experimental](https://img.shields.io/badge/Lifecycle-Experimental-339999)](https://github.com/bcgov/repomountie/blob/master/doc/lifecycle-badges.md)

<!-- badges: end -->

## bcdc-search-improvement-capstone

A UBC MDS Capstone project focused on a proof-of-concept of the application of natural language processing modeling to improve the user search experience of the [B.C. Data Catalogue](https://catalogue.data.gov.bc.ca/datasets).

### Project Status
Work In Progress

### Problem Statement
The *BC Data Catalogue* contains over 4,000 datasets with lots of useful information, available for anyone to use. Despite its wealth of information, users often faced difficulties in locating the datasets they needed, resulting in lower engagement with the platform. \
To address this issue, we used **SBERT** to implement **Semantic Search** on top of **Solr** search engine. Semantic search is an advanced NLP technique that focuses on understanding user intent rather than relying solely on specific keywords. \
The new search engine shows a significant improvement in search performance and has the ability to comprehend synonyms and phrases. It can also handle typing errors, making it more intuitive and user-friendly. 

### How to run?
1. install Java 8
2. install dependencies using conda
```
conda env create -f environment.yml
```
3. start Solr
```
bin/solr.cmd start
```
4. Run the streamlit app
```
streamlit run search_engine.py
```

### Data Sources
B.C. Data Catalogue text data: sourced directly from the [B.C. Data Catalogue](https://catalogue.data.gov.bc.ca/dataset/bc-data-catalogue-content) available under the [Open Government Licence - British Columbia](https://www2.gov.bc.ca/gov/content/data/open-data/open-government-licence-bc).

### Software

### Getting Help or Reporting an Issue

To report bugs/issues/feature requests, please file an [issue](https://github.com/bcgov/bcdc-search-improvement-capstone/issues/).

### How to Contribute

If you would like to contribute, please see our [CONTRIBUTING](CONTRIBUTING.md) guidelines.

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

### Dependencies
Solr is an open source search platform built on [Apache Lucene](https://lucene.apache.org/). We used Solr 6.6.6 in this project. The license for Solr can be found at solr/LICENSE.txt.\
We also used [Vector Scoring Plugin for Solr](https://github.com/saaay71/solr-vector-scoring) to calculate the distance between the query and the documents.

### License

```
Copyright 2023 Province of British Columbia

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an &quot;AS IS&quot; BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
```
