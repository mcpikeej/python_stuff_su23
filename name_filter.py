#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 12:54:05 2023

@author: emilyjmcpike
"""
import pandas as pd

data = pd.read_csv("/Users/emilyjmcpike/Honors Thesis Material/nonmasers_allwise_source.csv")

df = data.rename(columns = {'source_name_01_y': 'sourcename'}) #renamed for convenience

#name filters, accounts for diffenreces in name from different catalogs/surveys
df['sourcename'] = df['sourcename'].str.replace('-', '')
df['sourcename'] = df['sourcename'].str.replace('+', '')
df['sourcename'] = df['sourcename'].str.replace('.', '')
df['sourcename'] = df['sourcename'].str.replace('i', '')
df['sourcename'] = df['sourcename'].str.replace('tst', '')
df['sourcename'] = df['sourcename'].str.replace('test', '')
df['sourcename'] = df['sourcename'].str.replace('noactives', '')
df['sourcename'] = df['sourcename'].str.upper()
df['sourcename'] = df['sourcename'].str.replace('2MASX', '')
df['sourcename'] = df['sourcename'].str.replace('SDSS', '')
df['sourcename'] = df['sourcename'].str.replace('A', '')
df['sourcename'] = df['sourcename'].str.replace('B', '')
df['sourcename'] = df['sourcename'].str.replace('S', '')
df['sourcename'] = df['sourcename'].str.replace('0', '')
df['sourcename'] = df['sourcename'].str.replace('NED', '')
df['sourcename'] = df['sourcename'].str.replace('NED1', '')
df['sourcename'] = df['sourcename'].str.replace('NED2', '')


#for each galaxy, keep the entry closest to mid-ir crossmatch
df2 = df.sort_values('dist_x', ascending=True).drop_duplicates('sourcename').sort_index()

#display galaxies cut
df3 = data[~data.count2019_01.isin(df2.count2019_01)]
print(df3)

#revert to original name for book keeping
cleaned_name = pd.merge(df2, data[['count2019_01', 'source_name_01_y']], on='count2019_01', how='inner')
cleaned_name = cleaned_name[['count2019_01', 'source_name_01_y', 'ra_01', 'dec_01']]
cleaned_name = cleaned_name.rename(columns = {'source_name_01_y': 'sourcename'})
#cleaned_name.to_csv('/Users/emilyjmcpike/name_dup_removed_nonmaser.csv', index = False)