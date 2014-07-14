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


def contador(codigo):
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM Recetas WHERE fk_id_categoria =?"
    resultado = c.execute(query, [codigo])
    result = resultado.fetchall()
    i = 0
    for row in result:
        i = i+1
    #contados = result.rowcount()
    con.close()
    return i

def obtener_recetas():
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM recetas"
    resultado = c.execute(query)
    recetas = resultado.fetchall()
    con.close()
    return recetas

def buscarEditar(codigo):
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM categorias WHERE id_categoria = ?"
    resultado = c.execute(query, [codigo])
    producto = resultado.fetchall()
    con.commit()
    con.close()
    return producto

def obtiene_pais(pk):
    con = conectar()
    c = con.cursor()
    query = "SELECT nombre FROM pais WHERE id_pais = ?"
    resultado = c.execute(query, [pk])
    producto = resultado.fetchall()
    con.commit()
    con.close()
    return producto

def reescribeProducto(datos, cod2):
    con = conectar()
    c = con.cursor()
    id_cate = datos[0]
    nom = datos[1]
    descrip = datos[2]
    query = """UPDATE categorias SET id_categoria = ?
            ,nombre = ?
            ,descripcion = ?
            WHERE id_categoria = ?"""
    infonueva = (id_cate, nom, descrip, cod2)
    c.execute(query, infonueva)
    con.commit()


def insertarproductos(datos):
    con = conectar()
    c = con.cursor()
    query = """INSERT INTO categorias (id_categoria,nombre,descripcion) VALUES (?,?,?)"""
    c.execute(query, datos)
    con.commit()


def filtrarProductos(texto):
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM recetas WHERE nombre LIKE \"%{0}%\"".format(texto)
    resultado = c.execute(query)
    producto = resultado.fetchall()
    con.close()
    return producto


def infoFila2(codigo):
    """Funcion que retorna la informacion de una fila
    @return valores"""
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM recetas WHERE id_receta=?"
    resultado = c.execute(query, [codigo])
    infoFila = resultado.fetchall()
    con.close()
    for row in infoFila:
        valores = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]]
    return valores


def delete(codigo):
    exito = False
    con = conectar()
    c = con.cursor()
    query = "DELETE FROM categorias WHERE id_categoria = ?"
    try:
        resultado = c.execute(query, [codigo])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito
