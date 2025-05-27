import singer
import pandas as pd
import numpy as np

LOGGER = singer.get_logger()

schema = {
    "properties": {
        "fairings": {
            "type": ["object", "null"],
            "properties": {
                "reused": {"type": ["boolean", "null"]},
                "recovery_attempt": {"type": ["boolean", "null"]},
                "recovered": {"type": ["boolean", "null"]},
                "ships": {"type": "array", "items": {"type": ["string", "null"]}},
            },
        },
        "links": {
            "type": "object",
            "properties": {
                "patch": {
                    "type": "object",
                    "properties": {
                        "small": {"type": ["string", "null"]},
                        "large": {"type": ["string", "null"]},
                    },
                },
                "reddit": {
                    "type": "object",
                    "properties": {
                        "campaign": {"type": ["string", "null"]},
                        "launch": {"type": ["string", "null"]},
                        "media": {"type": ["string", "null"]},
                        "recovery": {"type": ["string", "null"]},
                    },
                },
                "flickr": {
                    "type": "object",
                    "properties": {
                        "small": {"type": "array", "items": {}},
                        "original": {"type": "array", "items": {}},
                    },
                },
                "presskit": {},
                "webcast": {"type": ["string", "null"]},
                "youtube_id": {"type": ["string", "null"]},
                "article": {},
                "wikipedia": {"type": ["string", "null"]},
            },
        },
        "static_fire_date_utc": {},
        "static_fire_date_unix": {},
        "net": {"type": ["boolean", "null"]},
        "window": {},
        "rocket": {"type": ["string", "null"]},
        "success": {"type": ["boolean", "null"]},
        "failures": {"type": "array", "items": {}},
        "details": {},
        "crew": {"type": "array", "items": {"type": "string"}},
        "ships": {"type": "array", "items": {}},
        "capsules": {"type": "array", "items": {"type": "string"}},
        "payloads": {"type": "array", "items": {"type": "string"}},
        "launchpad": {"type": ["string", "null"]},
        "flight_number": {"type": ["integer", "null"]},
        "name": {"type": ["string", "null"]},
        "date_utc": {"type": "string", "format": "date-time"},
        "date_unix": {"type": ["integer", "null"]},
        "date_local": {"type": ["string", "null"]},
        "date_precision": {"type": ["string", "null"]},
        "upcoming": {"type": ["boolean", "null"]},
        "cores": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "core": {"type": ["string", "null"]},
                    "flight": {"type": ["integer", "null"]},
                    "gridfins": {"type": ["boolean", "null"]},
                    "legs": {"type": ["boolean", "null"]},
                    "reused": {"type": ["boolean", "null"]},
                    "landing_attempt": {"type": ["boolean", "null"]},
                    "landing_success": {"type": ["boolean", "null"]},
                    "landing_type": {"type": ["string", "null"]},
                    "landpad": {"type": ["string", "null"]},
                },
            },
        },
        "auto_update": {"type": ["boolean", "null"]},
        "tbd": {"type": ["boolean", "null"]},
        "launch_library_id": {"type": ["string", "null"]},
        "id": {"type": "string"},
    }
}


def main():
    url = "https://api.spacexdata.com/v4/launches"
    df = pd.read_json(url)

    df = df.replace({np.nan: None})
    df["success"] = df["success"].apply(lambda x: bool(x) if pd.notnull(x) else None)

    records = df.to_dict(orient="records")

    singer.write_schema("launches", schema, "id")
    singer.write_records("launches", records)


if __name__ == "__main__":
    main()
