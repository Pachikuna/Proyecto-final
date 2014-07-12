#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3


def conectar():

    con = sqlite3.connect('usuarios.db')
    con.row_factory = sqlite3.Row
    return con


def busca_usuario(usuario="", contrasea=""):
    con = conectar()
    c = con.cursor()
    datos = (usuario, contrasea)
    query = """ SELECT * FROM Usuarios WHERE user=? and contraseña=?"""
    resultado = c.execute(query, datos)
    usuario = resultado.fetchall()
    con.close()

    return usuario

