import geo_utils as gu


class GeoguessrProfile:
    def __init__(self, datas: dict) -> None:
        datas = gu.flatten_dict(datas)
        for name, value in datas.items():
            setattr(self, name, value)

    def __repr__(self) -> str:
        return "\n".join([f"{k} : {v}" for k, v in vars(self).items()])


class GeoguessrStats:
    def __init__(self, datas: dict) -> None:
        datas = gu.flatten_dict(datas)
        for name, value in datas.items():
            setattr(self, name, value)

    def __repr__(self) -> str:
        return "\n".join([f"{k} : {v}" for k, v in vars(self).items()])


class GeoguessrChallenge:
    def __init__(self, datas: dict) -> None:
        datas = gu.flatten_dict(datas)
        for name, value in datas.items():
            setattr(self, name, value)

    def __repr__(self) -> str:
        return "\n".join([f"{k} : {v}" for k, v in vars(self).items()])


class GeoguessrScore:
    def __init__(self, datas: dict) -> None:
        datas = gu.flatten_dict(datas)
        for name, value in datas.items():
            setattr(self, name, value)

    def __repr__(self) -> str:
        return "\n".join([f"{k} : {v}" for k, v in vars(self).items()])


class GeoguessrMap:
    def __init__(self, datas: dict) -> None:
        datas = gu.flatten_dict(datas)
        for name, value in datas.items():
            setattr(self, name, value)

    def __repr__(self) -> str:
        return "\n".join([f"{k} : {v}" for k, v in vars(self).items()])
