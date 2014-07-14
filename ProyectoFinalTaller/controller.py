#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3


def conectar():
    con = sqlite3.connect('recetas')
    con.row_factory = sqlite3.Row
    return con

def obtener_categorias():
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM categorias"
    resultado = c.execute(query)
    cate = resultado.fetchall()
    con.close()
    return cate

def obtener_recetas():
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM recetas"
    resultado = c.execute(query)
    recetas = resultado.fetchall()
    con.close()
    return recetas

def obtiene_pais(pk):
    con = conectar()
    c = con.cursor()
    query = "SELECT nombre FROM pais WHERE id_pais = ?"
    resultado = c.execute(query, [pk])
    producto = resultado.fetchall()
    con.commit()
    con.close()
    return producto