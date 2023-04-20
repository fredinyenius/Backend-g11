
import { Prisma } from "../prisma.js";
export const registroUsuario = async (req, res) => {
    const data = req.body;

    try {
        const usuarioCreado = await Prisma.suario.create({ data: data });

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