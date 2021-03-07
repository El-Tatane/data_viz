import pandas as pd
from utils import CONFIG
from sklearn import preprocessing
from .decorator import singleton
from .referentiel import ordered_month_list


@singleton
class DataProcessing:

    def __init__(self, path=CONFIG["file"]["path"], col_date_list=CONFIG["file"]["date_col_list"]):
        self.df = pd.read_csv(path, parse_dates=col_date_list)

        self.df["rating-number"] = (self.df["rating-number"]
                                    .map(lambda x: x.replace(",", ".") if isinstance(x, str) else x)
                                    .astype({"rating-number": float}))

        # basic traitement

        self.add_column_total_earn()
        self.add_month()
        self.add_year()

    def add_column_total_earn(self):
        self.df["total_earn"] = self.df["num_subscribers"] * self.df["price"]

    def add_month(self):
        self.df["month"] = self.df["published_timestamp"].dt.strftime("%B")

    def add_year(self):
        self.df["year"] = self.df["published_timestamp"].dt.year

    def get_unique_value(self, col_name):
        if col_name in self.df.columns:
            return self.df[col_name].unique()
        else:
            raise IndexError(f"{col_name} not in df")

    def get_df(self):
        return self.df

    def normalize(self, df):
        x = df.values  # returns a numpy array
        min_max_scaler = preprocessing.MinMaxScaler()
        x_scaled = min_max_scaler.fit_transform(x)
        return pd.DataFrame(x_scaled, columns=df.columns)

    def get_radar_char(self):
        col = ["content_duration", "num_lectures", "price", "total_earn", "num_reviews"]
        sub_df = pd.DataFrame(columns=["direction", "type", "value"])

        normalize_df = self.normalize(self.df[col])

        for fun in "min", "mean", "max":
            tmp_df = getattr(normalize_df, fun)()
            print(tmp_df)
            for name, val in tmp_df.iteritems():
                sub_df = sub_df.append({"direction": name, "type": fun, "value": val}, ignore_index=True)

        return sub_df

    def get_bar_time_df(self, time_type, analysis_target="num_subscribers", data_filter_dict=None):
        df_filtered = self.get_data_filtered(data_filter_dict)
        if time_type == "year":
            return df_filtered[[analysis_target, time_type]].groupby(time_type).sum().reset_index()
        return df_filtered[[analysis_target, time_type]].groupby(time_type).sum().reindex(ordered_month_list, axis=0)\
            .reset_index()

    def get_parallel_coordinates_df(self, analysis_target, data_filter_dict):
        cols = ["num_lectures", "content_duration", "price", analysis_target]
        return self.get_data_filtered(data_filter_dict, cols=cols)

    def get_level_pie_chart_df(self, data_filter_dict):
        df = self.get_data_filtered(data_filter_dict, cols=["course_id", "level"])
        return (df.groupby("level").count()
                .reset_index().rename(columns={"course_id": "count"}))

    def get_subject_pie_chart_df(self, data_filter_dict):
        df_filter = self.get_data_filtered(data_filter_dict, cols=["course_id", "subject"])
        return (df_filter.groupby("subject").count()
                .reset_index().rename(columns={"course_id": "count"}))

    def get_target_hist_df(self, analysis_target, data_filter_dict):
        df_filter = self.get_data_filtered(data_filter_dict, cols=[analysis_target])
        return df_filter

    def get_bubble_chart_histogram_df(self, analysis_target, category, data_filter_dict):
        df_filter = self.get_data_filtered(data_filter_dict,
                                           cols=[analysis_target, category, "num_lectures", "content_duration"])
        return df_filter.dropna(axis="rows")

    def get_data_filtered(self, data_filter_dict, cols=None):
        cols = self.df.columns if cols is None else cols
        if data_filter_dict is None:
            try:
                return self.df[cols]
            except:
                print("gh", cols)
                return self.df[cols]
        real_data_filter_dict = {key: value for key, value in data_filter_dict.items() if key in self.df.columns}
        df_filter = self.df.copy()
        for key, value in real_data_filter_dict.items():
            if isinstance(value, list):
                df_filter = df_filter.loc[df_filter[key].isin(value)]
            else:
                df_filter = df_filter.loc[df_filter[key] == value]
        return df_filter[cols]
