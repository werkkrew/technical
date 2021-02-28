"""
Momentum indicators
"""

from numpy.core.records import ndarray


########################################
#
# Momentum Indicator Functions
#

# ADX                  Average Directional Movement Index
# ADXR                 Average Directional Movement Index Rating
# AO                   Awesome Oscillator
def ao(dataframe, sma1=5, sma2=34, field='hl2'):
    from .overlap_studies import sma
    dataframe = dataframe.copy()
    dataframe['hl2'] = (dataframe['high'] + dataframe['low']) / 2
    dataframe['ao'] = sma(dataframe, sma1, field) - sma(dataframe, sma2, field)
    return = dataframe['ao']


# APO                  Absolute Price Oscillator
# AROON                Aroon
# AROONOSC             Aroon Oscillator
# BOP                  Balance Of Power

# CCI                  Commodity Channel Index
def cci(dataframe, period) -> ndarray:
    from pyti.commodity_channel_index import commodity_channel_index

    return commodity_channel_index(dataframe['close'], dataframe['high'], dataframe['low'], period)


# CMO                  Chande Momentum Oscillator
def cmo(dataframe, period, field='close') -> ndarray:
    from pyti.chande_momentum_oscillator import chande_momentum_oscillator
    return chande_momentum_oscillator(dataframe[field], period)


# DX                   Directional Movement Index
# MACD                 Moving Average Convergence/Divergence
# MACDEXT              MACD with controllable MA type
# MACDFIX              Moving Average Convergence/Divergence Fix 12/26
# MFI                  Money Flow Index
# MINUS_DI             Minus Directional Indicator
# MINUS_DM             Minus Directional Movement

# MOM                  Momentum
def momentum(dataframe, field='close', period=9):
    from pyti.momentum import momentum as m
    return m(dataframe[field], period)


# PLUS_DI              Plus Directional Indicator
# PLUS_DM              Plus Directional Movement
# PPO                  Percentage Price Oscillator
# ROC                  Rate of change : ((price/prevPrice)-1)*100
# ROCP                 Rate of change Percentage: (price-prevPrice)/prevPrice
# ROCR                 Rate of change ratio: (price/prevPrice)
# ROCR100              Rate of change ratio 100 scale: (price/prevPrice)*100
# RSI                  Relative Strength Index
# STOCH                Stochastic
# STOCHF               Stochastic Fast
# STOCHRSI             Stochastic Relative Strength Index
def stochrsi(dataframe, period=14, field='close'):
    from pyti.stochrsi import stochrsi
    return stochrsi(dataframe[field], period)


# TRIX                 1-day Rate-Of-Change (ROC) of a Triple Smooth EMA

# ULTOSC               Ultimate Oscillator
def ultimate_oscilator(dataframe):
    from pyti.ultimate_oscillator import ultimate_oscillator as uo
    uo(dataframe['close'], dataframe['low'])
    return uo


# WILLR                Williams' %R
def williams_percent(dataframe, period=14, field='close'):
    highest_high = dataframe[field].rolling(period).max()
    lowest_low = dataframe[field].rolling(period).min()
    wr = (highest_high - dataframe[field]) / (highest_high - lowest_low) * -100
    return wr
