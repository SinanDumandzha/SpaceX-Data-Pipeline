import singer
import pandas as pd

LOGGER = singer.get_logger()

schema = {
    "properties": {
        "fairings": {"type": "null"},
        "links": {
            "type": "object",
            "properties": {
                "patch": {
                    "type": "object",
                    "properties": {
                        "small": {"type": "string"},
                        "large": {"type": "string"},
                    },
                },
                "reddit": {
                    "type": "object",
                    "properties": {
                        "campaign": {"type": "null"},
                        "launch": {"type": "string"},
                        "media": {"type": "null"},
                        "recovery": {"type": "null"},
                    },
                },
                "flickr": {
                    "type": "object",
                    "properties": {
                        "small": {"type": "array", "items": {}},
                        "original": {"type": "array", "items": {}},
                    },
                },
                "presskit": {"type": "null"},
                "webcast": {"type": "string"},
                "youtube_id": {"type": "string"},
                "article": {"type": "null"},
                "wikipedia": {"type": "string"},
            },
        },
        "static_fire_date_utc": {"type": "null"},
        "static_fire_date_unix": {"type": "null"},
        "net": {"type": "boolean"},
        "window": {"type": "null"},
        "rocket": {"type": "string"},
        "success": {"type": "boolean"},
        "failures": {"type": "array", "items": {}},
        "details": {"type": "null"},
        "crew": {
            "type": "array",
            "items": [
                {"type": "string"},
                {"type": "string"},
                {"type": "string"},
                {"type": "string"},
            ],
        },
        "ships": {"type": "array", "items": {}},
        "capsules": {"type": "array", "items": [{"type": "string"}]},
        "payloads": {"type": "array", "items": [{"type": "string"}]},
        "launchpad": {"type": "string"},
        "flight_number": {"type": "integer"},
        "name": {"type": "string"},
        "date_utc": {"type": "string"},
        "date_unix": {"type": "integer"},
        "date_local": {"type": "string"},
        "date_precision": {"type": "string"},
        "upcoming": {"type": "boolean"},
        "cores": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "core": {"type": "string"},
                        "flight": {"type": "integer"},
                        "gridfins": {"type": "boolean"},
                        "legs": {"type": "boolean"},
                        "reused": {"type": "boolean"},
                        "landing_attempt": {"type": "boolean"},
                        "landing_success": {"type": "boolean"},
                        "landing_type": {"type": "string"},
                        "landpad": {"type": "string"},
                    },
                }
            ],
        },
        "auto_update": {"type": "boolean"},
        "tbd": {"type": "boolean"},
        "launch_library_id": {"type": "string"},
        "id": {"type": "string"},
    }
}


def main():
    url = "https://api.spacexdata.com/v4/launches"
    df = pd.read_json(url)

    records = df.to_dict(orient="records")

    singer.write_schema("launches", schema, "id")
    singer.write_records("launches", records)


if __name__ == "__main__":
    main()
