#
import retentioneering

def data_vec(col_name):
    # update config to pass columns names:
    retentioneering.config.update({
        'user_col': 'deviceid',
        'event_col': col_name,
        'event_time_col': 'eventtime'
    })

    vec = data_1.rete.extract_features(feature_type='count',
                                     ngram_range=(1, 1))
    return vec

