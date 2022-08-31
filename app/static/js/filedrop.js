/*!
 * JS
 */
var func;
if (typeof funcClass === 'undefined') {
    var funcClass = function () {
        this.init();
    }
}

funcClass.prototype = {
    init: function () {
    },
    ready: function () {
        func.setDragFile();
    },
    loaded: function () {
    },
    setDragFile: function () {
        var fileArea = document.getElementById('dropArea');
        var fileInput = document.getElementById('uploadFile');

        fileArea.addEventListener('dragover', function (e) {
            e.preventDefault();
            fileArea.classList.add('dragover');
        });

        fileArea.addEventListener('dragleave', function (e) {
            e.preventDefault();
            fileArea.classList.remove('dragover');
        });

        fileArea.addEventListener('drop', function (e) {
            e.preventDefault();
            fileArea.classList.remove('dragover');
            var files = e.dataTransfer.files;
            fileInput.files = files;

            if (typeof files[0] !== 'undefined') {
                func.setFile(files[0]);
            } else {
                func.removeFile();
            }
        });

        fileInput.addEventListener('change', function (e) {
            var file = e.target.files[0];

            if (typeof e.target.files[0] !== 'undefined') {
                func.setFile(file);
            } else {
                func.removeFile();
            }
        }, false);
    },
    setFile: function (file) {
        var _upFileWrap = document.getElementById('upFileWrap');
        _upFileWrap.className = 'selected';

        var _name = document.getElementById('prevFile_name');
        var _type = document.getElementById('prevFile_type');
        var _size = document.getElementById('prevFile_size');

        console.log(file.name)
        _name.innerText = 'File Name = ' + file.name;
        _type.innerText = 'File Text = ' + file.type;
        _size.innerText = 'File Size = ' + file.size;

        //バックエンドにファイル送る処理とかとか
    },
    removeFile: function () {
        var _upFileWrap = document.getElementById('upFileWrap');
        _upFileWrap.className = '';

        var _name = document.getElementById('prevFile_name');
        var _type = document.getElementById('prevFile_type');
        var _size = document.getElementById('prevFile_size');

        _name.innerText = 'File Name = none';
        _type.innerText = 'File Name = none';
        _size.innerText = 'File Name = 0';
    }
};

func = new funcClass();

document.addEventListener("DOMContentLoaded", function (e) {
    func.ready();
});

window.addEventListener('load', function () {
    func.loaded();
});