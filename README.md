# Senior Design II – FONTAINE_DECAL  
**University of North Carolina at Charlotte**<br>
William States Lee College of Engineering  
**Author:** Ryan Monroe  

---

## History

| Date       | Update Description |
|------------|-------------------|
| 01/21/26   | Created project |
| 02/09/26   | Added projector on/off functionality |
| 02/16/26   | Added `pygame` to `requirements.txt`<br>Updated file structure |
| 02/23/26   | Revised GUI buttons to not navigate<br>Added new packages to `requirements.txt` (`Jinja2` for HTML)<br>Updated file structure to include new `index.html` containing GUI framework<br>Started movement functions in `scene.py` |
| 00/00/00   | n/a |

---

## File Structure
**Projector_Control/**
  * **app/**
      * `__init__.py` Python package indicator
      * `gui.py`Web-based user interface (FastAPI)
      * `controller.py` Abstracted projector commands
      * `serial_comm.py` Establish serial connection
      * **templates/**
          * `index.html` HTML framework for GUI
  * **display/**
      * `__init__.py` Python package indicator
      * `scene.py` Visualization of decals for projection (PyGame)
  * `requirements.txt` Dependencies list
  * `README.md` Projection documentation
