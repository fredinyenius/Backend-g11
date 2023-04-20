
import { Prisma } from "../prisma.js";
import bcrypt from "bcryptjs";
export const registroUsuario = async (req, res) => {
    // [ nombre : 'eduardo',apellido:'De Rivero', correo: 'xxxxxxx@gmail.com', pass]
    const data = req.body;

    try {
        const password = bcrypt.hashSync(data.password, 10)

        const usuarioCreado = await Prisma.usuario.create({
             data: {...data, password }
        });
        return res.status(201).json({
            message: "Usuario creado exitosamente",
        });
    }catch (error) {
        return res.status(500).json({
            message: "Error al crear el usuario",
            content: error.message,
        })
    }
};