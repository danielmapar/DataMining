# Second Class

* Data reduction --> removing un relevant data / reduce the size of data
  * This is the late step on the data preprocessing and it outputs the training data
Pattern extraction --> NN
Pattern evaluation --> Detect what useful information came from the extraction process

----------

## Transactional data

Pattern --> Frequent pattern (what kind of product combinations that costumers like to buy together)
Mostly commonly used for association

Transaction Data can vary in size compared to transactional data

Good for recommendation systems

Example: items could be a N size list (not a fixed size)


## Text Data

Set of documents --> articles, web pages, blogs, tweets, etc..
Structure --> highly unstructured (news, stories, etc.)
Semistructured --> HTML/XML documents

It is useful for text classification models (example: copy detection, emotion analysis)
keyword or content association --> Information retrieval

## Spatial data

Raster format --> Bitmap
Vector format --> consists of paths and points (Wont lose quality over resizing)
  * Great for images with for maps (line based images)

Find how an area changed over time


## Time Series data

Sequence of numeric values that changes over time
* Daily water consumption data in a city
  * More of a linear regression problem (predict future trends)


Sequence data (with your without clear notion of time)
***
Sequences of ordered objects or events (with or without concrete notation of time)
DNA is an example

Transaction would be a set of sequences compared to a stream data
Streaming data


## Graph Data

Molecular
The internet

We can find frequent subgraphs
  * Find communities in social networks
  * Predict social networks possible friendships


------

Predictive: Discover patterns on previous and current data in order to make predictions on future data
  * Classification (covered in class)
    * Finds a model (or function) from a set of pre-classified data objects
    * Labeled
    * Category prediction (find a class --> example: PlayTennis)
  * Regression
    * Linear model
    * Numeric prediction

Descriptive: Discover knowledge that characterizes general properties of data
  * Clustering (covered in class)
    * Group in different groups
    * Class label is unknown
    * Unsupervised learning
  * Concept characterization
  * Association analysis (frequent itemsets) - (covered in class)
    * support: among all transaction, 1% contains software
    * confidence: among the transactions contains computers, 75% contains software
  * Sequential pattern mining (covered in class)
    * Can also use it for recommendation

Predictive or descriptive
  * Time series analysis
  * Outlier detection (covered in class)
