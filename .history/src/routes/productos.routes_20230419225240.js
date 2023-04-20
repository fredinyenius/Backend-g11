import { Router } from "express";
import * as controllers from "../controllers/productos.controllers.js";
import { validarToken } from "../utils/wachiman.js";
export const productosRouter = Router();

productosRouter.post("/productos", validarToken, controllers.crearProducto);
