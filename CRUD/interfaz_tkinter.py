import tkinter as tk
from tkinter import ttk, messagebox
from typing import Optional
from servicio import Servicio
from controlador_servicios import ControladorServicios
from repositorio_servicios import RepositorioServicios

# Importar excepciones personalizadas
import sys
sys.path.append('..')
from exceptions.servicio_no_encontrado_error import ServicioNoEncontradoError
from exceptions.costo_invalido_error import CostoInvalidoError


class InterfazTkinter:
    
    def __init__(self, controlador: ControladorServicios):
        self.controlador = controlador
        self.root = tk.Tk()
        self.root.title("Sistema CRUD - Taller Mecánico")
        self.root.geometry("900x600")
        
        self._inicializar_componentes()
        self._crear_widgets()
        self._cargar_datos()
    
    def _inicializar_componentes(self):
        self.entry_cliente = None
        self.entry_vehiculo = None
        self.entry_tipo_servicio = None
        self.entry_costo = None
        self.entry_id = None
        self.treeview = None
    
    def _crear_widgets(self):
        # Frame principal
        frame_principal = ttk.Frame(self.root, padding="10")
        frame_principal.pack(fill=tk.BOTH, expand=True)
        
        # Frame de entrada de datos
        frame_entrada = ttk.LabelFrame(frame_principal, text="Datos del Servicio", padding="10")
        frame_entrada.pack(fill=tk.X, pady=(0, 10))
        
        # ID (solo lectura)
        ttk.Label(frame_entrada, text="ID:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_id = ttk.Entry(frame_entrada, width=10, state='readonly')
        self.entry_id.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        
        # Cliente
        ttk.Label(frame_entrada, text="Cliente:").grid(row=0, column=2, sticky=tk.W, padx=5, pady=5)
        self.entry_cliente = ttk.Entry(frame_entrada, width=30)
        self.entry_cliente.grid(row=0, column=3, sticky=tk.W, padx=5, pady=5)
        
        # Vehículo
        ttk.Label(frame_entrada, text="Vehículo:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_vehiculo = ttk.Entry(frame_entrada, width=30)
        self.entry_vehiculo.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        
        # Tipo de servicio
        ttk.Label(frame_entrada, text="Tipo Servicio:").grid(row=1, column=2, sticky=tk.W, padx=5, pady=5)
        self.entry_tipo_servicio = ttk.Entry(frame_entrada, width=30)
        self.entry_tipo_servicio.grid(row=1, column=3, sticky=tk.W, padx=5, pady=5)
        
        # Costo
        ttk.Label(frame_entrada, text="Costo ($):").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_costo = ttk.Entry(frame_entrada, width=15)
        self.entry_costo.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
        
        # Frame de botones
        frame_botones = ttk.Frame(frame_principal)
        frame_botones.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Button(frame_botones, text="Nuevo", command=self._limpiar_formulario).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botones, text="Guardar", command=self._guardar).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botones, text="Actualizar", command=self._actualizar).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botones, text="Eliminar", command=self._eliminar).pack(side=tk.LEFT, padx=5)
        
        # Treeview para mostrar datos
        frame_tabla = ttk.LabelFrame(frame_principal, text="Servicios Registrados", padding="10")
        frame_tabla.pack(fill=tk.BOTH, expand=True)
        
        columns = ('ID', 'Cliente', 'Vehículo', 'Tipo Servicio', 'Costo')
        self.treeview = ttk.Treeview(frame_tabla, columns=columns, show='headings', height=15)
        
        for col in columns:
            self.treeview.heading(col, text=col)
            self.treeview.column(col, width=150)
        
        self.treeview.column('Cliente', width=200)
        self.treeview.column('Vehículo', width=200)
        
        scrollbar = ttk.Scrollbar(frame_tabla, orient=tk.VERTICAL, command=self.treeview.yview)
        self.treeview.configure(yscroll=scrollbar.set)
        
        self.treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.treeview.bind('<<TreeviewSelect>>', self._seleccionar_servicio)
    
    def _cargar_datos(self):
        try:
            for item in self.treeview.get_children():
                self.treeview.delete(item)
            
            servicios = self.controlador.consultar_todos()
            
            for servicio in servicios:
                self.treeview.insert('', tk.END, values=(
                    servicio.id_servicio,
                    servicio.cliente,
                    servicio.vehiculo,
                    servicio.tipo_servicio,
                    f"${servicio.costo:.2f}"
                ))
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron cargar los datos: {str(e)}")
    
    def _limpiar_formulario(self):
        self.entry_id.config(state='normal')
        self.entry_id.delete(0, tk.END)
        self.entry_id.config(state='readonly')
        self.entry_cliente.delete(0, tk.END)
        self.entry_vehiculo.delete(0, tk.END)
        self.entry_tipo_servicio.delete(0, tk.END)
        self.entry_costo.delete(0, tk.END)
        self.entry_cliente.focus()
    
    def _seleccionar_servicio(self, event):
        seleccion = self.treeview.selection()
        
        if seleccion:
            item = self.treeview.item(seleccion[0])
            valores = item['values']
            
            self.entry_id.config(state='normal')
            self.entry_id.delete(0, tk.END)
            self.entry_id.insert(0, valores[0])
            self.entry_id.config(state='readonly')
            
            self.entry_cliente.delete(0, tk.END)
            self.entry_cliente.insert(0, valores[1])
            
            self.entry_vehiculo.delete(0, tk.END)
            self.entry_vehiculo.insert(0, valores[2])
            
            self.entry_tipo_servicio.delete(0, tk.END)
            self.entry_tipo_servicio.insert(0, valores[3])
            
            self.entry_costo.delete(0, tk.END)
            self.entry_costo.insert(0, valores[4].replace('$', ''))
    
    def _obtener_servicio_desde_formulario(self) -> Optional[Servicio]:
        try:
            id_texto = self.entry_id.get()
            id_servicio = int(id_texto) if id_texto else None
            
            costo = float(self.entry_costo.get())
            
            return Servicio(
                id_servicio=id_servicio,
                cliente=self.entry_cliente.get().strip(),
                vehiculo=self.entry_vehiculo.get().strip(),
                tipo_servicio=self.entry_tipo_servicio.get().strip(),
                costo=costo
            )
        except ValueError:
            messagebox.showerror("Error", "El costo debe ser un número válido")
            return None
    
    def _guardar(self):
        try:
            servicio = self._obtener_servicio_desde_formulario()
            
            if servicio is None:
                return
            
            if servicio.id_servicio is not None:
                messagebox.showwarning("Advertencia", "Use el botón Actualizar para modificar")
                return
            
            id_generado = self.controlador.registrar_servicio(servicio)
            messagebox.showinfo("Éxito", f"Servicio registrado con ID: {id_generado}")
            
            self._limpiar_formulario()
            self._cargar_datos()
            
        except CostoInvalidoError as e:
            messagebox.showerror("Error de Validación", str(e))
        except ServicioNoEncontradoError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar: {str(e)}")
    
    def _actualizar(self):
        try:
            servicio = self._obtener_servicio_desde_formulario()
            
            if servicio is None or servicio.id_servicio is None:
                messagebox.showwarning("Advertencia", "Seleccione un servicio de la tabla")
                return
            
            self.controlador.actualizar_servicio(servicio)
            messagebox.showinfo("Éxito", "Servicio actualizado correctamente")
            
            self._limpiar_formulario()
            self._cargar_datos()
            
        except CostoInvalidoError as e:
            messagebox.showerror("Error de Validación", str(e))
        except ServicioNoEncontradoError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo actualizar: {str(e)}")
    
    def _eliminar(self):
        try:
            id_texto = self.entry_id.get()
            
            if not id_texto:
                messagebox.showwarning("Advertencia", "Seleccione un servicio de la tabla")
                return
            
            id_servicio = int(id_texto)
            
            confirmacion = messagebox.askyesno(
                "Confirmar", 
                f"¿Está seguro de eliminar el servicio {id_servicio}?"
            )
            
            if confirmacion:
                self.controlador.eliminar_servicio(id_servicio)
                messagebox.showinfo("Éxito", "Servicio eliminado correctamente")
                
                self._limpiar_formulario()
                self._cargar_datos()
        
        except ServicioNoEncontradoError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar: {str(e)}")
    
    def ejecutar(self):
        self.root.mainloop()