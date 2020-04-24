import discord
import os
import datetime
import asyncio
from ftplib import FTP
import json
import logging
from discord.ext import commands
from discord.ext import tasks



class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# Special command. Info about Coronavirus! I wish you, your family, your friends and all users of this bot and their families and friends a lot of health <3 - Norxnd

    @commands.command(name="CovidInfo", aliases=["COVIDINFO", "covidinfo"])
    async def CovidInfo(self, ctx):
        Info = ("***--Novel 2019 Coronavirus---*** \n"
                "***APPLY FIVE PRINCIPLES*** \n"
                "**Help stop the coronavirus** \n"
                "1. *HAND* Wash them often with soap and water. \n"
                "2. *Elbow* Cover yourself when you cough. \n"
                "3. *FACE* Don't touch your eyes, nose or mouth. \n"
                "4. *DISTANCE* Keep a distance of 2 m. \n"
                "5. *SAFETY* Stay at home. \n"
                "\n")

        Info2 = ("There is currently no vaccine against coronavirus (COVID-19). \n"
                "To protect yourself and others from infection with the virus: \n"
                "Wash your hands regularly for 20 seconds with a soap and water or an alcohol-based disinfectant. \n"
                "When you cough or sneeze, cover your mouth and nose with a disposable tissue or the inside of your elbow. \n"
                "Avoid close (less than 1 meter) contact with people who feel unwell. \n"
                "If you feel unwell, do not leave the house and isolate yourself from other household members. \n"
                "Do not touch your eyes, nose or mouth when your hands are dirty. \n"
                "\n")

        Info3 = ("1-14 days may pass from infection to the onset of symptoms. The most common symptoms of coronavirus disease (COVID-19) are fever, fatigue and dry cough. Most people (about 80%) recover without the need for special treatment. \n"
                "In rarer cases, the disease is severe and can even be fatal. In the elderly and those with other conditions (such as asthma, diabetes or heart disease), coronavirus infection can lead to serious illness. \n"
                "Possible symptoms: \n"
                "cough, \n"
                "fever, \n"
                "fatigue, \n"
                "breathing difficulties (in severe cases). \n"
                "\n")

        Info4 = ("There is no medicine to prevent or treat coronavirus disease (COVID-19). Patients may require respiratory support. \n"
                "Self care \n"
                "If you have mild symptoms, do not leave the house until you recover. To relieve symptoms: \n"
                "rest and sleep a lot, \n"
                "bask in \n"
                "drink lots of fluids \n"
                "use a humidifier or take hot showers to ease coughing and a sore throat. \n"
                "Medical treatments \n"
                "If you develop a fever, cough or difficulty breathing, get medical help immediately. Notify your doctor in advance about your recent travels or contacts with people who have recently traveled. \n"
                "For more information, see who.int. \n")

        Info5 = ("***---Trusted and government websites about coronavirus---*** \n"
                 "*WHO (INT)* - https://www.who.int/health-topics/coronavirus#tab=tab_1 \n"
                 "*USA* - https://www.cdc.gov/coronavirus/2019-nCoV/index.html \n"
                 "*NORWAY* - https://helsenorge.no/koronavirus \n"
                 "*EUROPEAN UNION* - https://ec.europa.eu/info/live-work-travel-eu/health/coronavirus-response \n"
                 "*POLAND* - https://www.gov.pl/web/koronawirus \n"
                 "*CANADA* - https://www.canada.ca/en/public-health/services/diseases/coronavirus-disease-covid-19.html \n"
                 "*RUSSIA* - https://covid19.rosminzdrav.ru/ \n"
                 "*FRANCE* - https://www.gouvernement.fr/info-coronavirus \n"
                 "*GERMANY* - https://www.bundesregierung.de/breg-de/themen/coronavirus \n"
                 "*SPAIN* - https://www.mscbs.gob.es/profesionales/saludPublica/ccayes/alertasActual/nCov-China/home.htm \n"
                 "*BRAZIL* - https://coronavirus.saude.gov.br/ \n"
                 "*AUSTRALIA* - https://www.australia.gov.au/ \n")

        await ctx.send(Info, delete_after=120)
        await ctx.send(Info2, delete_after=120)
        await ctx.send(Info3, delete_after=120)
        await ctx.send(Info4, delete_after=120)
        await ctx.send(Info5, delete_after=120)
        LOG = ("{} used ?CovidInfo command with arguments: at {}".format(ctx.author, datetime.datetime.utcnow()))
        self.bot.BOT_LOG.append(LOG)



def setup(bot):
    bot.add_cog(Admin(bot))