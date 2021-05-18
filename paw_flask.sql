-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 17 Bulan Mei 2021 pada 04.35
-- Versi server: 10.4.13-MariaDB
-- Versi PHP: 7.4.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `paw_flask`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `community`
--

CREATE TABLE `community` (
  `namaKomunitas` varchar(100) NOT NULL,
  `urlKomunitas` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `community`
--

INSERT INTO `community` (`namaKomunitas`, `urlKomunitas`) VALUES
('IT World', 'https://t.me/ITWorld_ID');

-- --------------------------------------------------------

--
-- Struktur dari tabel `ebook`
--

CREATE TABLE `ebook` (
  `idFile` int(11) NOT NULL,
  `idUser` int(11) DEFAULT NULL,
  `judul` varchar(100) DEFAULT NULL,
  `type` varchar(80) DEFAULT NULL,
  `tahun` int(11) DEFAULT NULL,
  `file` varchar(250) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `relatecommunity`
--

CREATE TABLE `relatecommunity` (
  `namaKomunitas` varchar(100) DEFAULT NULL,
  `idUser` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `relatecommunity`
--

INSERT INTO `relatecommunity` (`namaKomunitas`, `idUser`) VALUES
('IT World', 1);

-- --------------------------------------------------------

--
-- Struktur dari tabel `user`
--

CREATE TABLE `user` (
  `idUser` int(11) NOT NULL,
  `namaUser` varchar(100) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `user`
--

INSERT INTO `user` (`idUser`, `namaUser`, `password`, `email`) VALUES
(1, 'akhfzz', '$5$rounds=535000$f4l', 'akhmadfaizal13@gmail');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `community`
--
ALTER TABLE `community`
  ADD PRIMARY KEY (`namaKomunitas`);

--
-- Indeks untuk tabel `ebook`
--
ALTER TABLE `ebook`
  ADD PRIMARY KEY (`idFile`),
  ADD KEY `idUser` (`idUser`);

--
-- Indeks untuk tabel `relatecommunity`
--
ALTER TABLE `relatecommunity`
  ADD KEY `namaKomunitas` (`namaKomunitas`),
  ADD KEY `idUser` (`idUser`);

--
-- Indeks untuk tabel `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`idUser`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `ebook`
--
ALTER TABLE `ebook`
  MODIFY `idFile` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT untuk tabel `user`
--
ALTER TABLE `user`
  MODIFY `idUser` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `ebook`
--
ALTER TABLE `ebook`
  ADD CONSTRAINT `ebook_ibfk_1` FOREIGN KEY (`idUser`) REFERENCES `user` (`idUser`);

--
-- Ketidakleluasaan untuk tabel `relatecommunity`
--
ALTER TABLE `relatecommunity`
  ADD CONSTRAINT `relatecommunity_ibfk_1` FOREIGN KEY (`namaKomunitas`) REFERENCES `community` (`namaKomunitas`),
  ADD CONSTRAINT `relatecommunity_ibfk_2` FOREIGN KEY (`idUser`) REFERENCES `user` (`idUser`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
