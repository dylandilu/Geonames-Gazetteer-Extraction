#-*- coding:utf-8 -*-
import os
import sys
import argparse

def il_geonames(lang,falna,dir_out,fGeonames):
    cadList={}
    with open(falna,'r') as f:
        for oneline in f:
            if oneline.strip().split('\t')[2]==lang:
                if oneline.strip().split('\t')[1] in cadList:
                    cadList[oneline.strip().split('\t')[1]].append(oneline.strip().split('\t')[3])
                else:
                    cadList[oneline.strip().split('\t')[1]]=[oneline.strip().split('\t')[3]]






    f_out=open(os.path.join(dir_out,'%s_geonames.txt'%lang),'w')

    geoDic={}
    n=0

    with open(fGeonames,'r') as f:
        for oneline in f:
            n+=1
            geonameid = oneline.split('\t')[0]
            name= oneline.split('\t')[1]
            asciiname = oneline.split('\t')[2]
            alternatenames = oneline.split('\t')[3]
            if geonameid in cadList:
                for onealt in cadList[geonameid]:
                    f_out.write('%s\t%s\n'%(onealt, name))
    f_out.close()

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Extracting gazetteer from Geonames')
    parser.add_argument('--target_language', default='zh', required = True, help='the 2-digit language code for target language')
    parser.add_argument('--output_directory', default='data/gaz/', help='the path of the folder to save the extracted lexicon')
    parser.add_argument('--path_allCountries', default='data/allCountries.txt', help='path of allCountries.txt')
    parser.add_argument('--path_alternateNames', default='data/alternateNames.txt', help='path of alternateNames.txt')
    args = parser.parse_args()

    il_geonames(args.target_language,args.path_alternateNames,args.output_directory,args.path_allCountries)
