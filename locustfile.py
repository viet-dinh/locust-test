import time
import random
import json
import locust.stats
from locust import HttpUser, task

locust.stats.CSV_STATS_INTERVAL_SEC = 1 # default is 1 second
locust.stats.CSV_STATS_FLUSH_INTERVAL_SEC = 10 # Determines how often the data is flushed to disk, default is 10 seconds
products = json.load(open('/mnt/locust/products.json','r'))
brands = json.load(open('/mnt/locust/brands.json','r'))

class QuickStartUser(HttpUser):
    url = "/"
    api_key = "da2-jovt32cveraqlhwd2tzqtfs7ie"

    @task(65)
    def plp(self):
        base_query = """
            query PLP {
                products (
                    filters: {
                        brand: {
                           include: [
                               "%brand%"
                           ],
                           exclude: [
                           ]
                        }
                    },
                    orderBy: CHEAPEST,
                    first: 40
                ) {
                    edges {
                        node {
                            __typename
                            ... on ProductDetail {
                                id
                                name
                                images
                                slug
                                brand {
                                    name
                                }
                                views
                                localPrice {
                                    minimum {
                                        sale
                                    }
                                }
                                keySpecs {
                                    name
                                    value
                                }
                                specifications {
                                    name
                                    value
                                }
                                characteristics {
                                    name
                                    value
                                }
                            }

                            ... on Offer {
                                id
                                name
                                stock
                                sku
                                deeplink
                                localPrice {
                                    original
                                    sale
                                    discount
                                    currency
                                }
                                internationalPrice {
                                    original
                                    sale
                                    discount
                                    currency
                                }
                                popularity
                                merchant {
                                    id
                                    name
                                    url
                                    deliveryHtml
                                    paymentMethods
                                    images
                                    offerId
                                    code
                                    feed
                                }
                                seller {
                                    name
                                    rating
                                }
                                rating
                                brand {
                                    name
                                    slug
                                    image
                                }
                                characteristics {
                                    name
                                    value
                                }
                                attributes {
                                    name
                                    value
                                }
                                shipping {
                                    location
                                    isOverseas
                                }
                                outOfStock
                                condition
                            }
                        }
                        cursor
                    }
                    pageInfo {
                        endCursor
                        hasNextPage
                    }
                    price {
                        minimum {
                            original
                            sale
                            discount
                            currency
                        }
                        average {
                            original
                            sale
                            discount
                            currency
                        }
                        maximum {
                            original
                            sale
                            discount
                            currency
                        }
                    }
                    totalCount
                    genders
                    brands {
                        id
                        name
                        slug
                        image
                    }
                    merchants {
                        id
                        name
                    }
                    categories {
                        id
                        name
                        slug
                        image
                    }
                    colors {
                        name
                        slug
                    }
                }
            }
        """

        random_brands = random.choice(brands)
        random_brand = random_brands['_source']['url']

        self.client.post(
            self.url,
            json={"query": base_query.replace("%brand%", random_brand)},
            headers={"x-api-key": self.api_key}
        )

    @task(35)
    def pdp(self):
        base_query = """
            query PDP {
                productDetail(name: "%name%") {
                    id
                    name
                    images
                    slug
                    brand {
                        slug
                        name
                        image
                    }
                    localPrice {
                        minimum {
                            sale
                        }
                    }
                    specifications {
                        name
                        value
                    }
                    offers(
                        first: 5,
                        filters: {
                        sellerRating: {
                            greaterThanOrEqual: 4.4
                            }
                        },
                        orderBy: CHEAPEST
                    ) {
                        edges {
                            node {
                                id
                                name
                                images
                                deeplink
                                localPrice {
                                    original
                                    sale
                                    discount
                                    currency
                                }
                                merchant {
                                    name
                                    deliveryHtml
                                    paymentMethods
                                    images
                                }
                                seller {
                                    name
                                    rating
                                }
                                brand {
                                    name
                                    slug
                                    image
                                }
                                shipping {
                                    location
                                    isOverseas
                                }
                            }
                            cursor
                        }
                        totalCount
                        merchants {
                            name
                        }
                    }

                    variants {
                        name
                        slug
                        characteristics {
                            name
                            value
                        }
                    }
                }
            }
        """

        random_product = random.choice(products)
        random_product_name = random_product['_source']['name']

        self.client.post(
            self.url,
            json={"query": base_query.replace('%name%', random_product_name)},
            headers={"x-api-key": self.api_key}
        )
