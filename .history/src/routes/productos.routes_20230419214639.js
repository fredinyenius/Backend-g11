import { Router } from "express";
import * as controllers from "../controllers/productos.controllers.js";

export const usuarioRouter = Router();

usuarioRouter.post("/productos", controllers.crearProducto);
