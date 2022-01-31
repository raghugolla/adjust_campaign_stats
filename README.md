# advertisement_analysis python project

Expose the sample dataset through a single generic HTTP API endpoint, which is capable of filtering, grouping and sorting.

Dataset represents performance metrics (impressions, clicks, installs, spend, revenue) for a given date, advertising channel, country and operating system.
Dataset is expected to be stored and processed in a relational database.

sample data set: https://gist.github.com/kotik/3baa5f53997cce85cc0336cb1256ba8b/

API should serve following data:

    1. filter by time range (date_from+date_to is enough), channels, countries, operating systems
    2. group by one or more columns: date, channel, country, operating system
    3. sort by any column in ascending or descending order
    4. see derived metric CPI (cost per install) which is calculated as cpi = spend / installs


## Usage

### Running the app

- `docker-compose up`

### Running tests

- `docker-compose run advertisement_analysis_web pytest`

## Structure
- db: contains schema/migrations
- advertisement_analysis: The actual project
    - api: controller layer
    - domain: domain model, services etc go here
    - exapi: Calls to external systems from this project
    - libraries: General purpose stuff
    - store: DB store
    - `__init__.py`: `create_app` which bootstraps the flask application
    - utils: General utility functions
        - `config.py`: Configurations setup
        - `flask.py`: Some modifications to flask
        - `log.py`: struct-log setup
        - `schema.py`: function wrapper to use voluptuous
- tests: All the tests
    - `conftest.py`: Basic fixtures
- `.drone.yml`: CD setup
- `pytest-fix.sh`: Fix if you switch between multiple environments multiple environments (host machine, docker, vm, etc.)
- `Pipfile`, `Pipfile.lock`: Requirements


## Frameworks/Libraries

### Web framework
- [Flask](http://flask.pocoo.org/)

### Metrics collection / tracing
- [datadog/statsd](https://github.com/DataDog/datadogpy)

### Database: [Postgres](https://www.postgresql.org/)
- [psycopg2](http://initd.org/psycopg/docs/)
- [sqlalchemy](https://www.sqlalchemy.org/)
- [sqlalchemy-utils](https://github.com/kvesteri/sqlalchemy-utils)
- [flask-sqlalchemy](http://flask-sqlalchemy.pocoo.org/2.3/)
- [alembic](http://alembic.zzzcomputing.com/en/latest/)
- [flask-migrate](https://flask-migrate.readthedocs.io/en/latest/)

## Schema verification
- [voluptuous](https://github.com/alecthomas/voluptuous)

## Testing
- pytest
- pytest-flask
- responses
- pytest-runner
- pytest-cov
- pytest-pep8

## Other
- stringcase - conversion of string cases
- colorama - pretty console output {NOTE: Only required for development}
  `pipenv install --dev` to install it.

## Run locally
 - Open command line
 - git clone https://github.com/raghugolla/adjust_campaign_stats.git
 - cd adjust_campaign_stats
 - docker-compose up

## Sample API Calls:


1. Show the number of impressions and clicks that occurred before the 1st of June 2017, broken down by channel and country, sorted by clicks in descending order.

Curl Request:


    curl -X GET \
      'http://0.0.0.0:9198/api/v1/search?group_by=channel%2Ccountry&to_time=2017-06-01&sum_of=clicks%2Cimpressions&order_by=clicks&order=DESC'

Http Request:

    http://0.0.0.0:9198/api/v1/search?group_by=channel,country&to_time=2017-06-01&sum_of=clicks,impressions&order_by=clicks&order=DESC

Response:

    {
        "data": [
            {
                "channel": "adcolony",
                "clicks": 13089,
                "country": "US",
                "impressions": 532608
            },
            {
                "channel": "apple_search_ads",
                "clicks": 11457,
                "country": "US",
                "impressions": 369993
            },
            {
                "channel": "vungle",
                "clicks": 9430,
                "country": "GB",
                "impressions": 266470
            },
            {
                "channel": "vungle",
                "clicks": 7937,
                "country": "US",
                "impressions": 266976
            },
            {
                "channel": "unityads",
                "clicks": 7374,
                "country": "US",
                "impressions": 215125
            },
            {
                "channel": "facebook",
                "clicks": 6282,
                "country": "DE",
                "impressions": 214725
            },
            {
                "channel": "google",
                "clicks": 6252,
                "country": "US",
                "impressions": 211378
            },
            .
            .
    
    ]
    }



2. Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order.

Curl Request:


    curl -X GET \
      'http://0.0.0.0:9198/api/v1/search?os=ios&group_by=os%2Ccampaign_date&from_time=2017-05-01&to_time=2017-05-31&sum_of=installs&order_by=campaign_date&order=ASC'

Http Request:


    http://0.0.0.0:9198/api/v1/search?os=ios&group_by=os,campaign_date&from_time=2017-05-01&to_time=2017-05-31&sum_of=installs&order_by=campaign_date&order=ASC

Response:


    {
        "data": [
            {
                "campaign_date": "2017-05-17T00:00:00+00:00",
                "installs": 755,
                "os": "ios"
            },
            {
                "campaign_date": "2017-05-18T00:00:00+00:00",
                "installs": 765,
                "os": "ios"
            },
            {
                "campaign_date": "2017-05-19T00:00:00+00:00",
                "installs": 745,
                "os": "ios"
            },
            {
                "campaign_date": "2017-05-20T00:00:00+00:00",
                "installs": 816,
                "os": "ios"
            },
            {
                "campaign_date": "2017-05-21T00:00:00+00:00",
                "installs": 751,
                "os": "ios"
            },
            {
                "campaign_date": "2017-05-22T00:00:00+00:00",
                "installs": 781,
                "os": "ios"
            },
            {
                "campaign_date": "2017-05-23T00:00:00+00:00",
                "installs": 813,
                "os": "ios"
            },
            {
                "campaign_date": "2017-05-24T00:00:00+00:00",
                "installs": 789,
                "os": "ios"
            },
            {
                "campaign_date": "2017-05-25T00:00:00+00:00",
                "installs": 875,
                "os": "ios"
            },
            {
                "campaign_date": "2017-05-26T00:00:00+00:00",
                "installs": 725,
                "os": "ios"
            },
            {
                "campaign_date": "2017-05-27T00:00:00+00:00",
                "installs": 712,
                "os": "ios"
            },
            {
                "campaign_date": "2017-05-28T00:00:00+00:00",
                "installs": 664,
                "os": "ios"
            },
            {
                "campaign_date": "2017-05-29T00:00:00+00:00",
                "installs": 752,
                "os": "ios"
            },
            {
                "campaign_date": "2017-05-30T00:00:00+00:00",
                "installs": 762,
                "os": "ios"
            },
            {
                "campaign_date": "2017-05-31T00:00:00+00:00",
                "installs": 685,
                "os": "ios"
            }
        ]
    }



3. Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order.

Curl Request: 


    curl -X GET \
      'http://0.0.0.0:9198/api/v1/search?countries=US&group_by=country%2Cos%2Ccampaign_date&from_time=2017-06-01&to_time=2017-06-01&sum_of=revenue&order_by=revenue&order=DESC'

Http Request:


    http://0.0.0.0:9198/api/v1/search?countries=US&group_by=country,os,campaign_date&from_time=2017-06-01&to_time=2017-06-01&sum_of=revenue&order_by=revenue&order=DESC


Sample Response:


    {
        "data": [
            {
                "campaign_date": "2017-06-01T00:00:00+00:00",
                "country": "US",
                "os": "android",
                "revenue": 1205.21
            },
            {
                "campaign_date": "2017-06-01T00:00:00+00:00",
                "country": "US",
                "os": "ios",
                "revenue": 398.87
            }
        ]
    }


4. Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order. Please think carefully which is an appropriate aggregate function for CPI.

Curl Request:


    curl -X GET \
      'http://0.0.0.0:9198/api/v1/search?countries=CA&sum_of=spend&group_by=channel&order_by=cpi&order=DESC&cpi=cpi'

Http Request:


    http://0.0.0.0:9198/api/v1/search?countries=CA&sum_of=spend&group_by=channel&order_by=cpi&order=DESC&cpi=yes

Sample Response:


    {
        "data": [
            {
                "channel": "facebook",
                "cpi": 2.0748663101604277,
                "spend": 1164
            },
            {
                "channel": "chartboost",
                "cpi": 2,
                "spend": 1274
            },
            {
                "channel": "unityads",
                "cpi": 2,
                "spend": 2642
            },
            {
                "channel": "google",
                "cpi": 1.7419860627177708,
                "spend": 999.9000000000004
            }
        ]
    }


## Few Other queries:


- get all the records whose os is `android`


    0.0.0.0:9198/api/v1/search?os=android


- get all the records whose os in `android, ios` and sort by clicks in descending order


    0.0.0.0:9198/api/v1/search?os=android,ios&order_by=clicks&order=DESC


- get all the records whose channels is `adcolony`
    0.0.0.0:9198/api/v1/search?channels=adcolony



